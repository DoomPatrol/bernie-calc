from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from app.forms import BernieCalcForm
from django.views.decorators.http import require_http_methods

from app.taxes import get_taxes
from app.income import calculate_healthcare_difference, calculate_overall_difference
from app.debt import calculate_debt_monthly_payment

# Create your views here.

class HomePageView(FormView):

  template_name = 'pages/home.html'
  form_class = BernieCalcForm
  success_url = reverse_lazy('calculator_results')


class CalculatorResultsView(View):

  template_name = 'app/calculator_results.html'
  # only allow post for this view
  http_method_names = ['post']

  def post(self, request):

    context_dict = {}
    yearly_income = int(request.POST.get('total_yearly_income'))

    context_dict['form_data'] = request.POST
    # healthcare calculations
    context_dict['current_taxes'] = get_taxes(yearly_income, request.POST.get('include_standard_deduction'), int(request.POST.get('number_of_children')), request.POST.get('tax_filing_status'), False)
    context_dict['bernie_taxes'] = get_taxes(yearly_income, request.POST.get('include_standard_deduction'), int(request.POST.get('number_of_children')), request.POST.get('tax_filing_status'), True)
    
    # medical debt calculations
    medical_debt = int(request.POST.get('medical_debt'))
    # divide by 1200 for 12 months * 100 (to get floating decimal of APR)
    medical_debt_monthly_apr = round(float(request.POST.get('medical_debt_interest_rate')) / 1200, 4)
    medical_debt_monthly_num_payments = round(int(request.POST.get('medical_debt_years_left')) * 12)
    context_dict['medical_debt'] = int(request.POST.get('medical_debt'))
    context_dict['medical_debt_payoff'] = calculate_debt_monthly_payment(medical_debt_monthly_apr, medical_debt_monthly_num_payments, medical_debt)

    # student loan calculations
    student_loans = int(request.POST.get('current_student_loans'))
    # divide by 1200 for 12 months * 100 (to get floating decimal of APR)
    student_loans_monthly_apr = round(float(request.POST.get('student_loans_interest_rate')) / 1200, 4)
    student_loans_monthly_num_payments = round(int(request.POST.get('student_loans_years_left')) * 12)
    context_dict['student_loans'] = int(request.POST.get('current_student_loans'))
    context_dict['student_loans_payoff'] = calculate_debt_monthly_payment(student_loans_monthly_apr, student_loans_monthly_num_payments, student_loans)

    # total debt calculations
    context_dict['debt'] = {}
    context_dict['debt']['total_debt'] = round(medical_debt + student_loans, 2)
    context_dict['debt']['monthly_debt_payments'] = round(context_dict['medical_debt_payoff'] + context_dict['student_loans_payoff'], 2)


    '''now we calculate the differences for statistics we want
      we want to calculate overall difference & healthcare difference
      Overall factors in no longer having student loans or healthcare debt
      '''
    total_healthcare_spending = round(round(int(request.POST.get('healthcare_monthly_premium')) * 12) + int(request.POST.get('yearly_healthcare_spending')))
    context_dict['total_yearly_spending'] = round(total_healthcare_spending + context_dict['medical_debt_payoff'] + context_dict['student_loans_payoff'], 2)
    context_dict['total_monthly_spending'] = round(context_dict['total_yearly_spending'] / 12, 2)
    context_dict['overall_difference'] = calculate_overall_difference(yearly_income, context_dict['total_yearly_spending'], context_dict['current_taxes'], context_dict['bernie_taxes'])
    context_dict['healthcare_difference'] = calculate_healthcare_difference(yearly_income, total_healthcare_spending, context_dict['current_taxes'], context_dict['bernie_taxes'])

    # let's create some friendly objects we can use for data viz
    context_dict['bernie_monthly_income_doughnut_data'] = {
      'monthly_taxes': round(context_dict['bernie_taxes']['breakdown']['total_taxes'] /12 , 2),
      'monthly_income': context_dict['overall_difference']['bernie_monthly_income_after_spending_and_taxes'],

    }

    context_dict['current_monthly_income_doughnut_data'] = {
      'monthly_healthcare_spending':  round(total_healthcare_spending / 12, 2),
      'monthly_taxes': round(context_dict['current_taxes']['breakdown']['total_taxes'] /12 , 2),
      'student_loans': context_dict['student_loans_payoff'],
      'medical_debt': context_dict['medical_debt_payoff'],
      'monthly_income': context_dict['overall_difference']['current_monthly_income_after_spending_and_taxes'],

    }
    return render(request, self.template_name, context_dict)


  def get_context_data(self, **kwargs):
    
    context = super().get_context_data(**kwargs)

    print(self.request.POST)

    return context

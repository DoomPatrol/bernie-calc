from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from app.forms import BernieCalcForm
from django.views.decorators.http import require_http_methods
from app.taxes import get_taxes

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
    context_dict['current_taxes'] = get_taxes(int(request.POST.get('total_yearly_income')), request.POST.get('include_standard_deduction'), int(request.POST.get('number_of_children')), request.POST.get('tax_filing_status'))
    return render(request, self.template_name, context_dict)


  def get_context_data(self, **kwargs):
    
    context = super().get_context_data(**kwargs)

    print(self.request.POST)

    return context

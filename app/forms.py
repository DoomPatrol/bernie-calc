from django import forms
from django.utils.translation import gettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Div

TAX_FILING_CHOICES = (
  ('single', _('Single')),
  ('married_jointly', _('Married Filing Jointly')),
  ('married_separately', _('Married Filing Seperately')),
  ('head_of_household', _('Head of Household')),
)


class BernieCalcForm(forms.Form):

  total_yearly_income = forms.IntegerField(help_text=_('Total Yearly Income for your household'),  min_value=0, max_value=1000000, initial=30000)
  tax_filing_status = forms.ChoiceField(help_text=_('Your tax filing status (helps us calculate taxes more accurately)'), choices=TAX_FILING_CHOICES, initial='single')
  include_standard_deduction = forms.BooleanField(required=False, help_text=_('Include the standard deduction in the calculation (recommended)'), initial=True)
  number_of_children = forms.IntegerField(help_text=_('Number of children in your household'), min_value=0, max_value=50, initial=0)
  health_care_monthly_premium = forms.IntegerField(help_text=_('Your current health care monthly premiums'), min_value=0, max_value=1000000, initial=250)
  yearly_health_care_spending = forms.IntegerField(help_text=_('How much do you spend per year on health care on top of your monthly premium. Think deductibles, perscription costs, bills not covered by insurance, etc.'), min_value=0, max_value=1000000, initial=2000)
  medical_debt = forms.IntegerField(help_text=_('How much do you currently have in medical debt'), min_value=0, max_value=1000000, initial=0)
  medical_debt_interest_rate = forms.FloatField(help_text=_('Your medical debt annual interest rate'), max_value=50, min_value=0, initial=0)
  medical_debt_years_left = forms.IntegerField(help_text=_('How many years do you have left to pay on your medical debt?'), min_value=1, max_value=30, initial=3)
  current_student_loans = forms.IntegerField(help_text=_('How much do you currently have in student loans'), min_value=0, max_value=1000000, initial=0)
  student_loans_interest_rate = forms.FloatField(help_text=_('Your student loans annual interest rate'), max_value=50, min_value=0, initial=5)
  student_loans_years_left = forms.IntegerField(help_text=_('How many years do you have left to pay on your student loans?'), min_value=1, max_value=30, initial=10)

  def __init__(self, *args, **kwargs):
    super(BernieCalcForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()

    self.helper.layout = Layout(
      Row(
        HTML("""
            <div class="col-12"><h3>Finances</h3></div>
        """),
        Column('total_yearly_income', css_class='form-group col-md-4 col-12 mb-0'),
        Column('tax_filing_status', css_class='form-group col-md-4 col-12 mb-0'),
        Column('number_of_children', css_class='form-group col-md-4 col-12 mb-0'),
        Column('include_standard_deduction', css_class='form-group col-md-6 col-12 mb-0'),
        css_class='form-row'
      ),
      Row(
        HTML("""
            <div class="col-12"><h3>Health Care</h3></div>
        """),
        Column('health_care_monthly_premium', css_class='form-group col-md-6 col-12 mb-0'),
        Column('yearly_health_care_spending', css_class='form-group col-md-6 col-12 mb-0'),
        css_class='form-row'
      ),
      Row(
        HTML("""
            <div class="col-12"><h3>Debt</h3></div>
        """),
        Column('medical_debt', css_class='form-group col-md-6 col-12 mb-0'),
        Column('current_student_loans', css_class='form-group col-md-6 col-12 mb-0'),
        css_class='form-row'
      ),
      Row(
        HTML("""
            <div class="col-12 text-right advanced-debt-selector"><p>Advanced Customization <i class="typcn typcn-arrow-sorted-down"></i></p></div>
        """),
          Column('medical_debt_interest_rate', css_class='form-group col-md-6 col-12 mb-0 advanced-debt-container'),
          Column('medical_debt_years_left', css_class='form-group col-md-6 col-12 mb-0 advanced-debt-container'),
          Column('student_loans_interest_rate', css_class='form-group col-md-6 col-12 mb-0 advanced-debt-container'),
          Column('student_loans_years_left', css_class='form-group col-md-6 col-12 mb-0 advanced-debt-container'),
        css_class='form-row'
      ),
    )
    self.helper.add_input(Submit('submit', 'See Your Results', css_class='btn secondary-button'))
    self.helper.form_method = 'POST'
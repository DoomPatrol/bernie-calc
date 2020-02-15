from django import forms
from django.utils.translation import gettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML

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
  healthcare_monthly_premium = forms.IntegerField(help_text=_('Your current healthcare monthly premiums'), min_value=0, max_value=1000000, initial=250)
  yearly_healthcare_spending = forms.IntegerField(help_text=_('How much do you spend per year on healthcare on top of your monthly premium. Think deductibles, medicine costs, etc.'), min_value=0, max_value=1000000, initial=2000)
  medical_debt = forms.IntegerField(help_text=_('How much do you currently have in medical debt'), min_value=0, max_value=1000000, initial=0)
  childcare_monthly_spending = forms.IntegerField(help_text=_('How much do you spend per month on child care costs'), min_value=0, max_value=1000000, initial=0)
  current_student_loans = forms.IntegerField(help_text=_('How much do you currently have in student loans'), min_value=0, max_value=1000000, initial=0)
  credit_card_debt = forms.IntegerField(help_text=_('How much do you currently have in credit card debt'), min_value=0, max_value=1000000, initial=0)

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
            <div class="col-12"><h3>Healthcare</h3></div>
        """),
        Column('healthcare_monthly_premium', css_class='form-group col-md-4 col-12 mb-0'),
        Column('yearly_healthcare_spending', css_class='form-group col-md-4 col-12 mb-0'),
        Column('medical_debt', css_class='form-group col-md-4 col-12 mb-0'),
        css_class='form-row'
      ),
      Row(
        HTML("""
            <div class="col-12"><h3>Childcare & Debt</h3></div>
        """),
        Column('childcare_monthly_spending', css_class='form-group col-md-4 col-12 mb-0'),
        Column('current_student_loans', css_class='form-group col-md-4 col-12 mb-0'),
        Column('credit_card_debt', css_class='form-group col-md-4 col-12 mb-0'),
        css_class='form-row'
      ),
    )
    self.helper.add_input(Submit('submit', 'See Your Results', css_class='btn secondary-button'))
    self.helper.form_method = 'POST'
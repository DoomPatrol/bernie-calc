from django import forms
from django.utils.translation import gettext as _

TAX_FILING_CHOICES = (
  ('single', _('Single')),
  ('married_jointly', _('Married Filing Jointly')),
  ('married_separately', _('Married Filing Seperately')),
  ('head_of_household', _('Head of Household')),
  ('widower', _('Qualified Widower')),
)


class HealthcareCostForm(forms.Form):

  total_yearly_income = forms.IntegerField(help_text=_('Your Total Monthly Income'), min_value=0, max_value=1000000)
  tax_filing_status = forms.ChoiceField(help_text=_('Your Total Monthly Income'), choices=TAX_FILING_CHOICES, default='single')
  current_monthly_premiums = forms.IntegerField(help_text=_('Your current monthly premiums'), min_value=0, max_value=1000000)
  current_yearly_spending = forms.IntegerField(help_text=_('How much do you spend per year on healthcare other than your monthly premium'), min_value=0, max_value=1000000)
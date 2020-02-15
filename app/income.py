''' 
let's use what we previously calculated tax wise to calculate differences between total current spending
and what income would look like under bernie
'''

def calculate_income_difference(yearly_income, healthcare_monthly_premium, healthcare_yearly_spending, current_taxes, medicare_for_all_taxes):

  income_breakdown_dict = {}
  # sum our monthly premium and extra spending
  income_breakdown_dict['yearly_total_healthcare_spending'] = round(round(healthcare_monthly_premium * 12) + healthcare_yearly_spending)
  income_breakdown_dict['current_income_after_healthcare'] = round(yearly_income - current_taxes['breakdown']['total_taxes'] - income_breakdown_dict['yearly_total_healthcare_spending']) 
  income_breakdown_dict['total_income_with_medicare_for_all'] = round(yearly_income - medicare_for_all_taxes['breakdown']['total_taxes'])
  income_breakdown_dict['income_difference'] = round(income_breakdown_dict['total_income_with_medicare_for_all'] - income_breakdown_dict['current_income_after_healthcare'])

  return income_breakdown_dict
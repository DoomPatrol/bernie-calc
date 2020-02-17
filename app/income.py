''' 
let's use what we previously calculated tax wise to calculate differences between total current spending
and what income would look like under bernie
'''
def calculate_overall_difference(yearly_income, total_current_spending, current_taxes, medicare_for_all_taxes):
  overall_difference_dict = {}
  overall_difference_dict['current_yearly_income_after_spending_and_taxes'] = round(yearly_income - current_taxes['breakdown']['total_taxes'] - total_current_spending, 2)
  overall_difference_dict['current_monthly_income_after_spending_and_taxes'] = round(overall_difference_dict['current_yearly_income_after_spending_and_taxes'] /12, 2)
  overall_difference_dict['bernie_yearly_income_after_spending_and_taxes'] = round(yearly_income - medicare_for_all_taxes['breakdown']['total_taxes'], 2)
  overall_difference_dict['bernie_monthly_income_after_spending_and_taxes'] = round(overall_difference_dict['bernie_yearly_income_after_spending_and_taxes'] / 12, 2)
  overall_difference_dict['yearly_difference'] = round(overall_difference_dict['bernie_yearly_income_after_spending_and_taxes'] - overall_difference_dict['current_yearly_income_after_spending_and_taxes'], 2)
  overall_difference_dict['monthly_difference'] = round(overall_difference_dict['yearly_difference'] / 12, 2)
  return overall_difference_dict


def calculate_healthcare_difference(yearly_income, yearly_total_healthcare_spending, current_taxes, medicare_for_all_taxes):

  income_breakdown_dict = {}
  # sum our monthly premium and extra spending
  income_breakdown_dict['yearly_total_healthcare_spending'] = yearly_total_healthcare_spending
  income_breakdown_dict['current_income_after_healthcare'] = round(yearly_income - current_taxes['breakdown']['total_taxes'] - income_breakdown_dict['yearly_total_healthcare_spending']) 
  income_breakdown_dict['total_income_with_medicare_for_all'] = round(yearly_income - medicare_for_all_taxes['breakdown']['total_taxes'])
  income_breakdown_dict['income_difference'] = round(income_breakdown_dict['total_income_with_medicare_for_all'] - income_breakdown_dict['current_income_after_healthcare'])
  income_breakdown_dict['tax_difference'] = round(medicare_for_all_taxes['breakdown']['total_taxes'] - current_taxes['breakdown']['total_taxes'], 2)
  return income_breakdown_dict
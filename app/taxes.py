# examples used are 2020 taxes
SINGLE_TAX_BRACKETS = [
  {'min': 0, 'max': 9875, 'tax_rate': .1},
  {'min': 9876, 'max': 40125, 'tax_rate': .12},
  {'min': 40126, 'max': 85525, 'tax_rate': .22},
  {'min': 85526, 'max': 163300, 'tax_rate': .24},
  {'min': 163301, 'max': 207350, 'tax_rate': .32},
  {'min': 207351, 'max': 518400, 'tax_rate': .35},
  {'min': 518401, 'max': None, 'tax_rate': .37},
]

MARRIED_FILING_JOINTLY_TAX_BRACKETS = [
  {'min': 0, 'max': 19750, 'tax_rate': .1},
  {'min': 19751, 'max': 80250, 'tax_rate': .12},
  {'min': 80251, 'max': 171050, 'tax_rate': .22},
  {'min': 171051, 'max': 326600, 'tax_rate': .24},
  {'min': 326601, 'max': 414700, 'tax_rate': .32},
  {'min': 414701, 'max': 622050, 'tax_rate': .35},
  {'min': 622051, 'max': None, 'tax_rate': .37},
]

MARRIED_FILING_SEPARATELY_TAX_BRACKETS = [
  {'min': 0, 'max': 9875, 'tax_rate': .1},
  {'min': 9876, 'max': 40125, 'tax_rate': .12},
  {'min': 40126, 'max': 85525, 'tax_rate': .22},
  {'min': 85526, 'max': 163300, 'tax_rate': .24},
  {'min': 163301, 'max': 207350, 'tax_rate': .32},
  {'min': 207351, 'max': 311025, 'tax_rate': .35},
  {'min': 518401, 'max': None, 'tax_rate': .37},
]

HEAD_OF_HOUSEHOLD_TAX_BRACKETS = [
  {'min': 0, 'max': 14100, 'tax_rate': .1},
  {'min': 14101, 'max': 53700, 'tax_rate': .12},
  {'min': 53701, 'max': 85500, 'tax_rate': .22},
  {'min': 85501, 'max': 163300, 'tax_rate': .24},
  {'min': 163301, 'max': 207350, 'tax_rate': .32},
  {'min': 207351, 'max': 518400, 'tax_rate': .35},
  {'min': 518401, 'max': None, 'tax_rate': .37},
]

BERNIE_SINGLE_TAX_BRACKETS = [
  {'min': 0, 'max': 9875, 'tax_rate': .1},
  {'min': 9876, 'max': 40125, 'tax_rate': .12},
  {'min': 40126, 'max': 85525, 'tax_rate': .22},
  {'min': 85526, 'max': 163300, 'tax_rate': .24},
  {'min': 163301, 'max': 207350, 'tax_rate': .32},
  {'min': 207351, 'max': 250000, 'tax_rate': .35},
  {'min': 250001, 'max': 500000, 'tax_rate': .40},
  {'min': 500001, 'max': 2000000, 'tax_rate': .45},
  {'min': 2000001, 'max': 10000000, 'tax_rate': .50},
  {'min': 10000001, 'max': None, 'tax_rate': .52},
]

BERNIE_MARRIED_FILING_JOINTLY_TAX_BRACKETS = [
  {'min': 0, 'max': 19750, 'tax_rate': .1},
  {'min': 19751, 'max': 80250, 'tax_rate': .12},
  {'min': 80251, 'max': 171050, 'tax_rate': .22},
  {'min': 171051, 'max': 326600, 'tax_rate': .24},
  {'min': 326601, 'max': 414700, 'tax_rate': .32},
  {'min': 414701, 'max': 500000, 'tax_rate': .35},
  {'min': 500001, 'max': 1000000, 'tax_rate': .40},
  {'min': 1000001, 'max': 4000000, 'tax_rate': .45},
  {'min': 4000001, 'max': 20000000, 'tax_rate': .50},
  {'min': 200000001, 'max': None, 'tax_rate': .52},
]

BERNIE_MARRIED_FILING_SEPARATELY_TAX_BRACKETS = [
  {'min': 0, 'max': 9875, 'tax_rate': .1},
  {'min': 9876, 'max': 40125, 'tax_rate': .12},
  {'min': 40126, 'max': 85525, 'tax_rate': .22},
  {'min': 85526, 'max': 163300, 'tax_rate': .24},
  {'min': 163301, 'max': 207350, 'tax_rate': .32},
  {'min': 207351, 'max': 250000, 'tax_rate': .35},
  {'min': 250001, 'max': 500000, 'tax_rate': .40},
  {'min': 500001, 'max': 2000000, 'tax_rate': .45},
  {'min': 2000001, 'max': 10000000, 'tax_rate': .50},
  {'min': 10000001, 'max': None, 'tax_rate': .52},
]

BERNIE_HEAD_OF_HOUSEHOLD_TAX_BRACKETS = [
  {'min': 0, 'max': 14100, 'tax_rate': .1},
  {'min': 14101, 'max': 53700, 'tax_rate': .12},
  {'min': 53701, 'max': 85500, 'tax_rate': .22},
  {'min': 85501, 'max': 163300, 'tax_rate': .24},
  {'min': 163301, 'max': 207350, 'tax_rate': .32},
  {'min': 207351, 'max': 250000, 'tax_rate': .35},
  {'min': 250001, 'max': 500000, 'tax_rate': .40},
  {'min': 500001, 'max': 2000000, 'tax_rate': .45},
  {'min': 2000001, 'max': 10000000, 'tax_rate': .50},
  {'min': 10000001, 'max': None, 'tax_rate': .52},
]


def get_taxes(income, standard_deduction, number_of_children, filing_status, bernie_calculation):

  taxes_dict = {}

  if standard_deduction and (filing_status == 'single' or filing_status == 'married_separately'):
    standard_deduction = 12400
    taxable_income = round(income - standard_deduction)
  elif standard_deduction and filing_status == 'married_jointly':
    standard_deduction = 24800
    taxable_income = round(income - standard_deduction)
  elif standard_deduction and filing_status == 'head_of_household':
    standard_deduction = 18650
    taxable_income = round(income - standard_deduction)
  else:
    standard_deduction = 0
    taxable_income = income
  
  child_tax_credit = round(number_of_children * 2000)
  taxable_income = round(taxable_income - child_tax_credit)

  # lets set all these variables so we can return them all togther
  taxes_dict['income'] = income
  taxes_dict['standard_deduction'] = standard_deduction
  taxes_dict['child_tax_credit'] = child_tax_credit
  taxes_dict['taxable_income'] = taxable_income

  if bernie_calculation:

    if filing_status == 'single':
      taxes_dict['breakdown'] = calculate_tax_breakdown(taxable_income, BERNIE_SINGLE_TAX_BRACKETS, True)
    
    elif filing_status == 'married_jointly':
      taxes_dict['breakdown'] = calculate_tax_breakdown(taxable_income, BERNIE_MARRIED_FILING_JOINTLY_TAX_BRACKETS, True)
    
    elif filing_status == 'married_separately':
      taxes_dict['breakdown'] = calculate_tax_breakdown(taxable_income, BERNIE_MARRIED_FILING_SEPARATELY_TAX_BRACKETS, True)
    
    else:
      taxes_dict['breakdown'] = calculate_tax_breakdown(taxable_income, BERNIE_HEAD_OF_HOUSEHOLD_TAX_BRACKETS, True)
  
  else:

    if filing_status == 'single':
      taxes_dict['breakdown'] = calculate_tax_breakdown(taxable_income, SINGLE_TAX_BRACKETS, False)
    
    elif filing_status == 'married_jointly':
      taxes_dict['breakdown'] = calculate_tax_breakdown(taxable_income, MARRIED_FILING_JOINTLY_TAX_BRACKETS, False)
    
    elif filing_status == 'married_separately':
      taxes_dict['breakdown'] = calculate_tax_breakdown(taxable_income, MARRIED_FILING_SEPARATELY_TAX_BRACKETS, False)
    
    else:
      taxes_dict['breakdown'] = calculate_tax_breakdown(taxable_income, HEAD_OF_HOUSEHOLD_TAX_BRACKETS, False)
  
  return taxes_dict

def calculate_tax_breakdown(taxable_income, tax_brackets, include_medicare_for_all):
  # Set up the items we need to then calculate on
  tax_breakdown_dict = {}
  tax_breakdown_dict['breakdown'] = []
  tax_breakdown_dict['total_taxes'] = 0
  break_loop = False

  for bracket in tax_brackets:

    # if no taxable income there won't be any taxes (free)
    if taxable_income <= 0:
      dollar_amount_to_tax = 0
      tax = 0
      break
  
    elif bracket['max'] and taxable_income > bracket['max']:
      # just get the max for this rate 
      dollar_amount_to_tax = round(bracket['max'] - bracket['min'])
      tax = round(dollar_amount_to_tax * bracket['tax_rate'])

    elif bracket['max'] is None or bracket['min'] <= taxable_income <= bracket['max']:
      # falls between the max and min or is exactly the max
      # first we need to see how much we need to tax
      dollar_amount_to_tax = round(taxable_income - bracket['min'])
      tax = round(dollar_amount_to_tax * bracket['tax_rate'])
      break_loop = True
      
    
    tax_breakdown_dict['breakdown'].append({
      'tax_level': '%s%%' % round(bracket['tax_rate'] * 100), 
      'amount_taxed_at_level': dollar_amount_to_tax,
      'taxes_paid': tax,
      'max': bracket['max'], 
      'min': bracket['min']
      })
    
    tax_breakdown_dict['total_taxes'] += tax
    
    # break loop if you no longer need to calculate
    # this is a bit redundant for top tax brackets but allows us to shorten code
    if break_loop:
      break
  
  if include_medicare_for_all and taxable_income <= 0:
    tax_breakdown_dict['medicare_for_all_tax'] = 0
    tax_breakdown_dict['total_taxes'] = 0
  elif include_medicare_for_all:
    tax_breakdown_dict['before_medicare_for_all'] = round(tax_breakdown_dict['total_taxes'])
    tax_breakdown_dict['medicare_for_all_tax'] = round(taxable_income * .04)
    tax_breakdown_dict['total_taxes'] = round(tax_breakdown_dict['total_taxes'] + tax_breakdown_dict['medicare_for_all_tax'])
  
  return tax_breakdown_dict
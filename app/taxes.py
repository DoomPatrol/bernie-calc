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


def get_taxes(income, standard_deduction, filing_status):

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

  if filing_status == 'single':
    return calculate_tax_breakdown(taxable_income, standard_deduction, SINGLE_TAX_BRACKETS)
  
  elif filing_status == 'married_jointly':
    return calculate_tax_breakdown(taxable_income, standard_deduction, MARRIED_FILING_JOINTLY_TAX_BRACKETS)
  
  elif filing_status == 'married_separately':
    return calculate_tax_breakdown(taxable_income, standard_deduction, MARRIED_FILING_SEPARATELY_TAX_BRACKETS)
  
  else:
    return calculate_tax_breakdown(taxable_income, standard_deduction, HEAD_OF_HOUSEHOLD_TAX_BRACKETS)

def calculate_tax_breakdown(taxable_income, standard_deduction, tax_brackets):
  # Set up the items we need to then calculate on
  tax_breakdown_dict = {}
  tax_breakdown_dict['breakdown'] = []
  tax_breakdown_dict['taxable_income'] = taxable_income
  tax_breakdown_dict['standard_deduction'] = standard_deduction
  tax_breakdown_dict['total_taxes'] = 0
  break_loop = False

  for bracket in tax_brackets:
    if bracket['max'] and taxable_income > bracket['max']:
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
  
  return tax_breakdown_dict
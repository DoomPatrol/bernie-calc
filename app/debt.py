
def calculate_debt_monthly_payment(monthly_apr, number_of_months, balance):
  print(monthly_apr, number_of_months, balance)
  # if balance is 0, this means they have no debt and don't need the calculation so just return 0
  if balance == 0:
    monthly_payment = 0
  
  # if they have interest free debt we only have to take the balanc / number of months
  if monthly_apr == 0:
    monthly_payment = round(balance / number_of_months, 2)
  # else do a calculation for 
  else:
    top =  monthly_apr * ((float(1) + monthly_apr) ** number_of_months)
    bottom = (((float(1) + monthly_apr) ** number_of_months)- 1)
    print('top', top, bottom)
    monthly_payment = round(balance * (top / bottom), 2)
  return monthly_payment
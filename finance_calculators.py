#Program for users to access one of two financial calculators: an investment calculator or a home loan repayment calculator

#Pseudo code:
#Import math
#Ask the user if they want to calculate interest or a bond and save this as a variable
#If the user wants to calculate interest
# ask the user to input the amount they are depositing and store this as a float
# ask the user to input the percentage of the interest rate and store this as a float
# ask the user to input the number of years they want to invest for and store this as an integer
# ask the user if they want simple or compound interest and store this as a variable called "interest"
# if they want simple interest
#   calculate the amount of interest they will recieve using the simple interest formula
# else if they want compound interest
#   calculate the amount of interest they will recieve using the compound interst formula
# print the amount of interest
#Else if the user wants to calculate a bond
# ask the user to input the present value of the house and store this as a float
# ask the user to input the percentage of the interest rate and store this as a float
# ask the user to input the number of months they plan to take to repay the bond
# calculate the monthly repayment amount
# print the monthly repayment amount

import math

#Asking user if interest or bond:
print("""Investment \t - to calculate the amount of interest you'll earn on your investment \n
Bond \t \t - to calculate the amount you'll have to pay on a home loan \n \n
Please enter either 'investment' or 'bond' from the menu above to proceed:""")
calc = input("")
calc = calc.lower()

#Calculating bond or investment amount:
#Investment:
if calc == "investment":
  P = float(input("Please enter the amount you would like to invest: "))
  i = float(input("Please enter the percentage of the interest rate: "))
  r = i/100
  t = int(input("Please enter the number of years you plan on investing for: "))
  interest = input("Would you like simple or compund interest? Please enter 'simple' or 'compound': ")
  interest = interest.lower()
  #Simple interest calculation
  if interest == "simple":
    A = P *(1 + r*t)
    print(f"Your total return with simple interest is R{round(A,2)} after {t} years at a {i}% interest rate")
  #Compound interest calculation:
  elif interest == "compound":
    A = P * math.pow((1+r),t)
    print(f"Your total return with compound interest is R{round(A,2)} after {t} years at a {i}% interest rate")
  else:
    print("Invalid input. Please try again.")
#Bond:
elif calc == "bond":
  P = float(input("Please enter the present value of the house: "))
  ai = float(input("Please enter the percentage of the annual interest rate: "))
  i = ai/(100*12)
  n = int(input("Please enter the number of months over which you would like to repay the bond: "))
  repayment = (i * P)/(1 - (1 + i)**(-n))
  print(f"Your monthly repayments are R{round(repayment,2)} for a {ai}% annual interest rate paid over {n} months.")
else:
  print("Invalid input. Please try again.")
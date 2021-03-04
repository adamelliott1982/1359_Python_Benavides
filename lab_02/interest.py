#   Program:    interest.py
#   Programmer: Adam Elliott
#   Date:      1/23/2021
#   Description:    Lab 2 - interest on loan
########################################

#declare vars
years = 15
rate = 6
loan = 5000

#perform calcs
interest = loan * (rate/100) * years

# show output

print()
print(f"Loan amount: \t${loan:,.2f}")
print(f"Interest rate: \t{rate}%")
print(f"No. of years: \t{years}")
print(f"Interest paid: \t${interest:,.2f}")
print()

#verify var type
print(type(interest))
print()
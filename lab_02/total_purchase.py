# Program Name: total_purchase.py
# Programmer: Adam Elliott
# Date: 1/24/2021
# Description: lab 2 part 2 - calculating sales tax
##########################################################

#groceries
apple = 1
milk = 3
wine = 10
cereal = 4.50

#sales tax
TAX_RATE = .06

#program name
print("Program: Total Purchase")
print()

#list of items
print(f"Item #1 - apple: \t${apple:>7,.2f}")
print(f"Item #2 - milk: \t${milk:>7,.2f}")
print(f"Item #3 - wine: \t${wine:>7,.2f}")
print(f"Item #4 - cereal: \t${cereal:>7,.2f}")


#dividing line
print("===============================================")

#calculations/output
subtotal = apple + milk + wine + cereal
print(f"Subtotal: \t\t${subtotal:>7.2f}")

sales_tax = TAX_RATE * subtotal
print(f"Sales tax: \t\t${sales_tax:>7,.2f}")

grand_total = subtotal + sales_tax
print(f"Grand total: \t\t${grand_total:>7.2f}")
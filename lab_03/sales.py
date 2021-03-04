# Program: sales.py
# Programmer: Adam Elliott
# Date: 02/05/2021
# Description: Lab 3 part 2 - calculate increase in sales
#################################################################

# initialize list of days of week starting with Monday abbreviated lowercase
days_of_week = ['mon','tue','wed','thu','fri','sat','sun']
# initialize daily sales list corresponding to days of week
daily_sales = [1000, 2000, 3000, 4000, 5000, 6000, 7000]


# print report header – Sales Report
print("ACME Stores Incorporated Sales Report:\n")
# print current sales with formatted days and sales as currency

print("Current Sales:\n")
print(f"{days_of_week[0].title()}: \t${daily_sales[0]:,.2f}")
print(f"{days_of_week[1].title()}: \t${daily_sales[1]:,.2f}")
print(f"{days_of_week[2].title()}: \t${daily_sales[2]:,.2f}")
print(f"{days_of_week[3].title()}: \t${daily_sales[3]:,.2f}")
print(f"{days_of_week[4].title()}: \t${daily_sales[4]:,.2f}")
print(f"{days_of_week[5].title()}: \t${daily_sales[5]:,.2f}")
print(f"{days_of_week[6].title()}: \t${daily_sales[6]:,.2f}")

# print projected 5% increase in sales using same formatting as before
print("\nProjected 5% increase:\n")
print(f"{days_of_week[0].title()}: \t${daily_sales[0] * 1.05:,.2f}")
print(f"{days_of_week[1].title()}: \t${daily_sales[1] * 1.05:,.2f}")
print(f"{days_of_week[2].title()}: \t${daily_sales[2] * 1.05:,.2f}")
print(f"{days_of_week[3].title()}: \t${daily_sales[3] * 1.05:,.2f}")
print(f"{days_of_week[4].title()}: \t${daily_sales[4] * 1.05:,.2f}")
print(f"{days_of_week[5].title()}: \t${daily_sales[5] * 1.05:,.2f}")
print(f"{days_of_week[6].title()}: \t${daily_sales[6] * 1.05:,.2f}\n")
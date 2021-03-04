# Program: rainfall_stats.py
# Programmer: Adam Elliott
# Date: 02/26/2021
# Description: lab 4 - track changing rainfall stats
###################################################


# initialize a list with names of the months all lowercase abbreviated
month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']


# initialize a list with average monthly rainfall corresponding to months
month_rain = [1.90, 2.37, 3.06, 3.20, 5.15, 3.23, 2.12, 2.03, 2.42, 4.11, 2.57, 2.57]

# print report header – Average Monthly Rainfall
print('Average Monthly Rainfall - 2018 - Dallas, TX\n')

# use range function to loop through both lists – pass len of month list
for value in range(len(month_rain)):
    # print month and average rainfall by accessing temporary variable
    print(f'{month_list[value].title()}\t{month_rain[value]:.2f}in.')
    
# print credit line showing source of data
print('\nSource: www.rssweather.com')

# use sum function to find the total rainfall and assign to total variable
total_rainfall = sum(month_rain)

# dividing total by len function of list and assign to average variable
average_rainfall = total_rainfall / len(month_rain)

# display total and average rainfall for year
print()
print(f'Total rainfall: \t{total_rainfall:.2f}')
print(f'Average rainfall: \t{average_rainfall:>5.2f}')
print()


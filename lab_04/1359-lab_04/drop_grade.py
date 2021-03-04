# Program: drop_grade.py
# Programmer: Adam Elliott
# Date: 02/26/2021
# Description: lab 4 - lists and for statements
########################################################


# create list of 5 grades and initialize
grades = [100, 80, 70, 60, 90]

# print report name – DROP LOWEST GRADE PROGRAM
print('DROP LOWEST GRADE PROGRAM:\n')

# show original grades using for in Loop
print('Grades:')
for grade in grades:
    print(grade)

# use sum function on grades to calculate the total
total = sum(grades)

# calculate the average by dividing total by len(grades)
average = total/len(grades)

# print number of grades using len function
print(f'Number of grades: {len(grades)}')

# print average formatted to 2 decimal places
print(f'Average: {average:.2f}')

# find the lowest grade using min function and print lowest grade
lowest_grade = min(grades)
print(f'Lowest grade: {lowest_grade}')

#remove lowest grade
grades.remove(lowest_grade)

# print LOWEST GRADE DROPPED
print('\nLOWEST GRADE DROPPED:\n')

# show grades after dropping lowest grade using for in Loop
print('Grades:')
for grade in grades:
    print(grade)

# use sum function to calculate the total after dropping lowest grade
total = sum(grades)

# compute new average
average = total/len(grades)

# print new number of grades
print(f'Number of grades: {len(grades)}')

# print new average
print(f'Average: {average:.2f}')

# find new lowest grade and print
lowest_grade = min(grades)
print(f'Lowest grade: {lowest_grade}')

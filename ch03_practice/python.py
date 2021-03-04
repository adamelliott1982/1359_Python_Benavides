
######################################################working with lists
# # pizzas = ['pepperoni', 'cheese', 'sausage']

# for pizza in pizzas:
#     print(f"\nI like {pizza} pizza.")

# print(f"\nI really love pizza!")
    
###################################################range function
# for value in range(1,6):
#     print(value)
    

# numbers = list(range(1,6))
# print(numbers)


# threes = list(range(3, 30, 3))
# print(threes)


# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)
# print(squares)

# prices = [4.99, 5, 27.89]
# print(sum(prices))

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# numbers = list(range(1,1000))
# print(numbers)

# for value in range(1, 101):
#     print(value)

# numbers = list(range(1,10000))
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for odd in range(1, 20, 2):
#     print(odd)

# print()

# for number in range(3, 30, 3):
#     print(number)


##################################################list comprehension (uses loop in list creation)
# cubes = [value ** 3 for value in range(1,11)]
# print(cubes)



############################################################# working with slices
characters = ['charles', 'martina', 'michael', 'florence', 'eli', 'jacob', 'stone', 'flash', 'saito']
# print(characters)

# print("My companions will be:")
# for companion in characters[:3]:
#     print(companion.title())


# dopelgangers = characters[:]
# print(f"Dopelgangers: {dopelgangers}\n")

# characters.append('adam')
# dopelgangers.append('sean')
# print(characters)
# print(dopelgangers)

# first_three = characters[:3]
# print(f'The first three characters are: ')
# for character in first_three:
#         print(character)

# second_three = characters[3:6]
# print(f'The second three characters are: ')
# for character in second_three:
#         print(character)

# last_three = characters[6:]
# print(f'The last three characters are: ')
# for character in last_three:
#         print(character)


##########################tuple - immutable lists
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# menu_items = ('spaghetti', 'ribs', 'milksteak')
# for item in menu_items:
#     print(item)

# print()

# menu_items = ('cheese', 'rice', 'milksteak')
# for item in menu_items:
#     print(item)



############################skipping list items
# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[0::2]) #prints odd numbers
# print(numbers[1::2]) #prints even numbers


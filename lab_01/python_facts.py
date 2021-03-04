# Program: python_facts.py
# Programmer: Adam Elliott
# Date: 1/21/2021
# Description: hello world exercise
#############################################

first_name = "adam"
last_name = "elliott"
python_creator = "Guido van Rossum"

message = f"My name is {first_name.title()} {last_name.title()}.\n"
# message2 = "My name was {} {}.\n".format(first_name.title(), last_name.title())
# message3 = f"My name shall be {first_name} {last_name}.".title()
# message4 = "My name was never "+first_name.title()+" "+last_name.title()+"."

print(message)
print("Things I've learned about Python:")
print("\n\tPython is a general purpose programming language.")
print(f"\tPython was created by {python_creator.title()} and released in 1991.")
print()
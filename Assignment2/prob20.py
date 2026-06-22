"""
i have printed the multiplication table of  7 by calling the function print_table
and use a for loop inside to multiply with the number 1 to 10 and print it out.
"""
def print_table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
    
print("Multiplication Table of 7:")
print_table(7)
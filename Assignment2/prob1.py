"""
i created a list of 5 numbers then used for loop and a variable to seperately take each
list number and add it to total and then printed out the final sum of the list numbers.
"""
numbers = [12, 5, 8, 20, 3]
total = 0
for num in numbers:
    total += num
print("Sum of all numbers:", total)
"""
I created a list of numbers and called the function and sent the list where
using a loop i calculated the sum and return it where it called and printed the sum.
"""
def sum_of_list(numbers):
    total = 0
    for item in numbers:
        total += item
    return total

list = [10, 20, 30, 40]
result = sum_of_list(list)
print("Total sum of the list:", result)
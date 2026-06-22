"""
i have taken a list of number and then used a loop to seperately check them
if they are greater then 10  or not and printed the count of greater numbers.
"""
num_list = [4, 15, 8, 23, 42, 10, 7]
counter = 0
for num in num_list:
    if num > 10:
        counter +=1
print("Count of numbers greater than 10:", counter)
"""
create a function count_down in loop range have -1 which helps to print the number reverse
or downward and called the function with the number i want to print till 0.
"""
def count_down(n):
    for i in range(n, 0, -1):
        print(i)

print("Countdown :")
count_down(4)
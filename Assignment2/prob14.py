"""
i have taken a number as input then used nested if else to check if it is positive
or not then if positive printed it's positive and checked if it is even/odd and if negetive 
then cheked 0/less then 0 and printed negetive or zero.
"""
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
    if(number % 2 == 0):
        print("It is also an even number.")
    else:
        print("It is also an odd number.")
else:
    if number < 0:
        print("The number is negetive.")
    else:
        print("The number is Zero.")
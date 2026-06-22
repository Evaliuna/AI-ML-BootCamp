"""
To check if the number is negetive or positive and even/odd i used nested loop
as logic if the taken input is more then zero then positive and if remainder is 0 then it is even.
"""
n = float(input("Enter a number: "))
result = 'Postitive' if n > 0 else ('Negative' if n < 0 else 'Zero')
print(f"The number is {result}")

if n == 0:
    print("The number is Zero, so it is neither even nor odd in this check.")
else:
    if n % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")
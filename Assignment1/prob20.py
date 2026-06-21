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
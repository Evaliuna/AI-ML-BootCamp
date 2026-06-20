num1 = 25
check1 = (num1 >= 10) and (num1 <= 50)
print(f"Is {num1} between 10 and 50? {check1}")

response = 'haha'
check2 = (response == 'yes') or (response == 'no')
print(f"Is '{response}' either 'yes' or 'no' ? {check2}")

num2 = 7
check3 = not (num2 % 2 == 0)
print(f"Is {num2} not divisible by 2? {check3}")
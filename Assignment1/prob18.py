score = int(input("Enter your score (0-100): "))

if score >= 90 and score <= 100:
    grade = 'A+'
elif score >= 80:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 40:
    grade = 'C'
else:
    grade = 'F'

if score >= 40:
    status = 'Pass'
else:
    status = 'Fail'
print(f"Grade: {grade}")
print(f"Status: {status}")
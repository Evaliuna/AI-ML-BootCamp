"""
Taking marks as input used nested if else to check if pass or fail then checked
if pass then which grade and printed the grade with.
"""
marks = int(input("Enter student's marks: "))

if marks >= 40:
    print("Result: Pass")
    if(marks >= 80):
        grade = "A"
    elif marks >= 60:
        grade = "B" 
    else:
        grade = "C"
    print(f"Grade: {grade}")
else:
    print("Result: Fail")
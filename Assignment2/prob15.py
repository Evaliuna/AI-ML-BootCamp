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
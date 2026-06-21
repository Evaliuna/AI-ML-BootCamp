"""
I have taking input age then checking if adult or minor while if adult and more then 60 age
then he/she is a senior citizen.
"""
age = int(input("Enter your age: "))

if age > 18:
    print("You are an adult.")
    if age > 60:
        print("Status: Senior Citizen")
else:
    print("You are a minor.")
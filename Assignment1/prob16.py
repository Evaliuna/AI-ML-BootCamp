"""
I took input using input() frist name then birth year as instructed. and then 
as 2025 current year calculated the age and print it using print(f"").
"""
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year
print(f"Hello {name}! You are approximately {age} years old.")
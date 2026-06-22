"""
I have stored user name and pass word. and then take input from the user to check 
if it is correct or wrong and finally printout a massage according to that.
"""
username = "admin"
password = "password123"

user_input_name = input("Enter username: ")
user_input_pass = input("Enter password: ")

if user_input_name == username:
    if user_input_pass == password:
        print("Access Granted")
    else:
        print("Wrong Password")
else:
    print("User Not Found")
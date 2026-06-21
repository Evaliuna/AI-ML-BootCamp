correct_username = "admin"
correct_password = "password123"

user_input_name = input("Enter username: ")
user_input_pass = input("Enter password: ")

if user_input_name == correct_username:
    if user_input_pass == correct_password:
        print("Access Granted")
    else:
        print("Wrong Password")
else:
    print("User Not Found")
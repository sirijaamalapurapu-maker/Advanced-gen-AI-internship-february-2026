# Correct credentials
correct_username = "admin"
correct_password = "1234"

# User given input
username = input("Enter username: ")
password = input("Enter password: ")

# Checking
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Credentials")
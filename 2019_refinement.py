# Q6
firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
username = firstname[:3] + lastname
print("Your username is " + username)

# Q7
while True:
    password = input("Please enter a password: ")
    if len(password) >= 8:
        break
    else:
        print("Password has to be 8 characters or more")

# Q8
while True:
    reenter = input("Please reenter your password: ")
    if reenter == password:
        print("Your password has been set.")
        break
    else:
        print("Password entries do not match. Please repeat the second entry of your password: ")


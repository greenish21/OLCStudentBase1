'''
# Challenge 1:
Write a function `validate_nric(nric: str) -> bool` to 
validate if a given input is a valid Singapore NRIC number. 
A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
and ends with an uppercase letter.

* In this case, assume that as long as the last character 
is an uppercase letter it is valid.

Normal Test: Input: "S1234567D", Output: True
Error Test: Input: "A1234567D", Output: False
Boundary Test: Input: "S123456", Output: False
'''
# NRIC = input("Enter your NRIC number: ")
# if NRIC[-1].isupper():
#     print("Output: True")
# else:
#     print("Output: False")
'''
# Challenge 2:
Write a function `is_valid_username(username: str) -> bool` to 
check if a username is correctly generated. A valid username 
should be at least 6 characters long, should not contain any spaces, 
and must start with an uppercase letter followed by lowercase letters.

Normal Test: Input: "Johndoe", Output: True
Error Test: Input: "johnDoe", Output: False
Error Test: Input: "John Doe", Output: False
Boundary Test: Input: "John", Output: False
'''
username = input("Enter your username: ")

if len(username) >= 6:
    length = True
else:
    length = False

if username.find(" ") == -1:
    space = True
else:
    space = False

if username[0].isupper():
    first_upper = True
else:
    first_upper = False

last_lower = True
for i in username[1:]:
    if not i.islower():
        last_lower = False

if length and space and first_upper and last_lower:
    print("Output: True")
else:
    print("Output: False")
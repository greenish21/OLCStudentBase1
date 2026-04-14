##############################################################
##### MOCK QUESTION ##########################################
##############################################################
# The task is to write a program that checks whether a food item has expired based on 
# its expiry date and today’s date. Dates are entered in the format "DD-MM".

# All code should have appropriate comments and meaningful identifiers. [2]
# 
# ________________________________________
# Task 5.1 [4]
# Write a calculate_days( ) function that accepts a date parameter in the format "DD-MM".
# The function must calculate and return the total number of days elapsed since 01-01, 
# assuming 30 days per month
# ________________________________________
'''
def calculate_days(expiry):
    day = expiry[:2]
    month = expiry[3:]
    if day[0] == 0:
        elapsed_d = int(day[1:2]) - 1
    else:
        elapsed_d = int(day) - 1

    if month[0] == 0:
        elapsed_m = int(month[1:2]) - 1
    else:
        elapsed_m = (int(month) - 1) * 30

    total = elapsed_d + elapsed_m
    return f"Total number of days since 01-01 is {total}"

print(calculate_days(input("Enter your date: ")))
'''










# Test your code using the values below
# print(calculate_days("01-02"))
# print(calculate_days("30-01"))
# print(calculate_days("30-02"))
# print(calculate_days("30-12"))


# ________________________________________
# Task 5.2  [3]
# Write a days_difference( ) function that takes two parameters:
# •	today (format "DD-MM")
# •	expiry (format "DD-MM")

# The function will check if an item has expired and return the number of days 
# between today’s date and the expiry date.
# •	Expiry is calculated by subtracting the today’s date from the expiry date. 
# You must use the calculate_days() function to retrieve the number of days between 
# today’s date and expiry date. Note that the number of days could be negative.
# You can assume both dates are always within the same year.
# 
# ________________________________________
'''
def calculate_days(expiry):
    day = expiry[:2]
    month = expiry[3:]
    
    if day[0] == '0':
        elapsed_d = int(day[1:2]) - 1
    else:
        elapsed_d = int(day) - 1

    if month[0] == '0':
        elapsed_m = (int(month[1:2]) - 1) * 30
    else:
        elapsed_m = (int(month) - 1) * 30

    total = elapsed_d + elapsed_m
    return total


def days_difference(today, expiry):
    today_days = calculate_days(today)
    expiry_days = calculate_days(expiry)
    
    difference = expiry_days - today_days
    
    return difference

print(days_difference("10-04", "15-04"))
'''

    


















# ________________________________________
# Task 5.3 [8]
# Write a validate_date( ) function that accepts one parameter:
# •	date_str (a string in the format "DD-MM")
# The function must check whether the input date is valid according to the following rules:
# 1.	The input must contain a dash (-) separator between day and month.
# 2.	Both the day (DD) and month (MM) must be two characters long (e.g. "05-04" not "5-4").
# 3.	The day (DD) must be between 1 and 30 (inclusive).
# 4.	The month (MM) must be between 1 and 12 (inclusive).
# If all conditions are met, the function should return True.
# If any condition fails, the function should return False.
# Displays appropriate messages for invalid input. You may assume the input is always a string.
# ________________________________________
def validate_date():
    if 

def calculate_days(expiry):
    day = expiry[:2]
    month = expiry[3:]
    
    if day[0] == '0':
        elapsed_d = int(day[1:2]) - 1
    else:
        elapsed_d = int(day) - 1

    if month[0] == '0':
        elapsed_m = (int(month[1:2]) - 1) * 30
    else:
        elapsed_m = (int(month) - 1) * 30

    total = elapsed_d + elapsed_m
    return total


def days_difference(today, expiry):
    today_days = calculate_days(today)
    expiry_days = calculate_days(expiry)
    
    difference = expiry_days - today_days
    
    return difference

print(days_difference("10-04", "15-04"))
















# print(validate_date("01#01"))
# print(validate_date("aa-01"))
# print(validate_date("01-aa"))
# print(validate_date("50-01"))
# print(validate_date("05-50"))
# print(validate_date("0310"))

# ________________________________________
# Task 5.4 [6]
# Create a simple text-based user interface that:
# •	Prompts and validates today’s date in "DD-MM" format.
# o	You must use the validate_date() function to validate today’s date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Prompts and validates the expiry date in "DD-MM" format.
# o	You must use the validate_date() function to validate the expiry date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Compute if the item has expired. You must use the days_difference() function. 
#     If the number of days is positive, the item has not expired. 
#          Output “Item is fresh and will expire in  days.”
#     If the number of days is negative, the item has expired. 
#          Output “Item has expired  days ago.”
#     If the number of days is 0, then the item expires today. 
        #    Output “Item will expire today!”
# ________________________________________

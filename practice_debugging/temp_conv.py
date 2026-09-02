
# Task 3
# The following program converts a range of Fahrenheit temperature readings
# to Celsius and vice versa. It begins by allowing the user to choose between
# an “F” for Fahrenheit to Celsius conversion or “C” for Celsius to Fahrenheit conversion.
# The program will print out the chosen conversions from the start value to the end value (inclusive).
# The formula for converting Fahrenheit to Celsius is:
#        C = 5/9 x ( F – 32 )
# The formula for converting Celsius to Fahrenheit is:
#        F = 32 + ( C * 9/5 )


def displayWelcome():
    print("This program will convert a range of temperatures")
    print("Enter (F) to convert Fahrenheit to Celsius")
    print("Enter (C) to convert Celsius to Fahrenheit\n")

def getConvertTo():
    which = input("Enter selection: ") # 1) Closed input
    while which != "F" and which != "C": # 3) Format error # 4) Changed to catch non F and C
        which = input("Enter selection: ") # 2) Indentation error
    return which

def displayFahrenToCelsius(start, end):
    print("\n Degrees", " Degrees")
    print("Fahrenheit", "Celsius")

    for temp in range(start, end + 1):
        converted_temp = temp - 32 * 5/9
        print("{:4.1f}      {:4.1f}".format(temp, converted_temp)) # 8) Changed temp to converted_temp

def displayCelsiusToFahren(start, end):
    print("\n Degrees", "Degrees")
    print(" Celsius", "Fahrenheit")

    for temp in range(start, end):
        converted_temp = 9/5 * temp * 32
        print("{:4.1f}      {:4.1f}".format(temp, converted_temp))

# --- main

#Display program welcome
displayWelcome()

# Get which conversion from user
which = getConvertTo() # 5) Changed temp_start to which

# Get range of temperatures to convert
temp_start = int(input("Enter starting temperature to convert: "))
temp_end = int(input("Enter ending temperature to convert: ")) # 6) Added int

# Display range of converted temperatures
if which == "F":  # 7) Swapped functions
    displayFahrenToCelsius(temp_start, temp_end)
elif which == "C":
    displayCelsiusToFahren(temp_start, temp_end)


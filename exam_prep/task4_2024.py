def div_2(number): 
    halved = int(number/2) 
    return halved

# Task 4.1 - Check OK - 5 marks
def odd_or_even(number):
    remainder = number % 2
    if remainder == 1:
        return "Odd"
    else:
        return "Even"

# Task 4.2
def prime(number):
    if number <= 1:
        return "Not prime"
    if number == 2:
        return "Prime"
    if odd_or_even(number) == 'Even':
        return "Not prime"
    for i in range (3, div_2(number)+1):
        if number % i == 0:
            return "Not prime"
    return "Prime"
# Task 4.3
while True:
    user_input = input("Enter only enter a whole number: ")
    if user_input.isdigit() == True:
        integer = int(user_input)
        if prime(integer) == "Prime":
            print(f"{integer} is a prime number")
        else:
            print(f"{integer} is not a prime number")   
    else:
        print("Please enter a valid number")
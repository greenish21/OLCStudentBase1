def div_2(number):
      halved = int(number/2)
      return halved

# Q10
def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Q11
def prime(number):
    half_num = div_2(number)
    count = 3
    if number == 2:
        return "prime"
    elif number < 2:
        return "not prime"
    elif odd_or_even(number) == "Odd":
        while count <= half_num:
            if number % count == 0:
                return "not prime"
            count += 1
        return "prime"
    else:
        return "not prime"

while True:
    number = int(input("Enter a whole number: "))
    if type(number) == int:
        break
    else:
        print("Enter a whole number only.")
print(f"{number} is {prime(number)}.")


        


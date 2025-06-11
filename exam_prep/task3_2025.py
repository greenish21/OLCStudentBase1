age = 0
height = float(0) 
rejected = 0 # 7. Changed rejected to 0
rider = 0
age = int(input("Please enter your age")) # 1. added missing quotation mark
height = float(input("Please enter your height "))
while height != 0 or age != 0: # 3. Changed <>

    if age <= 7 or age > 70 or height <= 1.3: # 9. Changed age to <=
        if age < 7:
            print("You are too young to ride") 
        if age > 90:
            print("You are too old to ride") 
        if height <= 1.3:
            print("You are too short to ride") 
        rejected = rejected + 1 # 6. changed rejected to +1
    else: # 2. Missing indent
        print("You can ride the Roller Coaster") 
        rider = rider + 1 # 5. Rider to rider
# 4. Removed extra input
print("Number of people rejected ", rejected) # 8. switched rider and rejected
print("Number of riders ", rider)

# Task 2 
# The following program is written for prospective customers 
# of a painting services company. 
# 
# The program provides a price quotation for the 
# painting services after customers enter their selection.
#==========================================================
'''
print("Welcome to ColorBest Painting Services!")
apartment = input("Select apartment type (A)3-room, (B)4-room:")
if apartment == "A":
    no_rooms = 3
elif apartment == "B":
    no_rooms = 4
    
paint_type = input("Select paint package (A)Easy-clean, (B)Mould-free:")

if paint_type == "A":
    base_cost = 1200
elif paint_type == "B":
    base_cost = 1800
    
colour_type = []
for i in range(1,no_rooms+1):
    paint_colour = input("Select paint color(01 to 58) for Room {}:".format(i))
    colour_type += [paint_colour]
    
print("Colours selected are:")
j = 1
for colour in colour_type:
    print("Color code for Room {0}: {1}".format(j,colour))
    j += 1
'''
#==========================================================
# 7	The company will extend their services to 5-room apartments. 
#   5-room apartments consist of 5 rooms in total.
#   Edit the program so that it allows users of 5-room apartments 
#   to enter that as a selection.	[2]
#==========================================================
'''
print("Welcome to ColorBest Painting Services!")
apartment = input("Select apartment type (A)3-room, (B)4-room, (C)5-room:")
if apartment == "A":
    no_rooms = 3
elif apartment == "B":
    no_rooms = 4
elif apartment == "C":
    no_rooms = 5
paint_type = input("Select paint package (A)Easy-clean, (B)Mould-free:")

if paint_type == "A":
    base_cost = 1200
elif paint_type == "B":
    base_cost = 1800
    
colour_type = []
for i in range(1,no_rooms+1):
    paint_colour = input("Select paint color(01 to 58) for Room {}:".format(i))
    colour_type += [paint_colour]
    
print("Colours selected are:")
j = 1
for colour in colour_type:
    print("Color code for Room {0}: {1}".format(j,colour))
    j += 1
'''





#==========================================================
# 8	The company has just added a third paint package 
#   “Premier all-in-one” to its existing list of services. 
#   Edit the program so that it allows users to select the 
#   “Premier all-in-one” package. The base cost of the package is $2200.	[2]
#==========================================================
'''
print("Welcome to ColorBest Painting Services!")
apartment = input("Select apartment type (A)3-room, (B)4-room, (C)5-room:")
if apartment == "A":
    no_rooms = 3
elif apartment == "B":
    no_rooms = 4
elif apartment == "C":
    no_rooms = 5
paint_type = input("Select paint package (A)Easy-clean, (B)Mould-free, (C)Premier all-in-one:")

if paint_type == "A":
    base_cost = 1200
elif paint_type == "B":
    base_cost = 1800
elif paint_type == "C":
    base_cost = 2200
    
colour_type = []
for i in range(1,no_rooms+1):
    paint_colour = input("Select paint color(01 to 58) for Room {}:".format(i))
    colour_type += [paint_colour]
    
print("Colours selected are:")
j = 1
for colour in colour_type:
    print("Color code for Room {0}: {1}".format(j,colour))
    j += 1
'''




#==========================================================
# 9	The customer is required to enter the colour codes for all the rooms. 
#   The colour code must be an integer between 1 to 58 (inclusive). 
#   Edit the program so that it validates the colour code entry and 
#   prompts for the colour code to be entered again each time 
#   an invalid colour code is entered.	[4]
#==========================================================
'''
print("Welcome to ColorBest Painting Services!")
apartment = input("Select apartment type (A)3-room, (B)4-room, (C)5-room:")
if apartment == "A":
    no_rooms = 3
elif apartment == "B":
    no_rooms = 4
elif apartment == "C":
    no_rooms = 5
paint_type = input("Select paint package (A)Easy-clean, (B)Mould-free, (C)Premier all-in-one:")

if paint_type == "A":
    base_cost = 1200
elif paint_type == "B":
    base_cost = 1800
elif paint_type == "C":
    base_cost = 2200
    
colour_type = []
for i in range(1,no_rooms+1):
    while True:    
        paint_colour = int(input("Select paint color(01 to 58) for Room {}:".format(i)))
        if paint_colour >= 1 and paint_colour <= 58:
            colour_type += [paint_colour]
            break
        else:
            print("Invalid input. Please enter again")

print("Colours selected are:")
j = 1
for colour in colour_type:
    print("Color code for Room {0}: {1}".format(j,colour))
    j += 1
'''




#==========================================================
# 10	The total cost of the painting service package 
#   includes the base cost and a variable cost. 
#   The variable cost depends on the total number of rooms to be painted,
#   with $120 charged per room to the total cost. 

#   Edit the program so that it computes the total package price 
#   and displays it at the end of the program.	[2]
#==========================================================
print("Welcome to ColorBest Painting Services!")
apartment = input("Select apartment type (A)3-room, (B)4-room, (C)5-room:")
if apartment == "A":
    no_rooms = 3
elif apartment == "B":
    no_rooms = 4
elif apartment == "C":
    no_rooms = 5
paint_type = input("Select paint package (A)Easy-clean, (B)Mould-free, (C)Premier all-in-one:")

if paint_type == "A":
    base_cost = 1200
elif paint_type == "B":
    base_cost = 1800
elif paint_type == "C":
    base_cost = 2200
    
colour_type = []
for i in range(1,no_rooms+1):
    while True:    
        paint_colour = int(input("Select paint color(01 to 58) for Room {}:".format(i)))
        if paint_colour >= 1 and paint_colour <= 58:
            colour_type += [paint_colour]
            break
        else:
            print("Invalid input. Please enter again")
print("Colours selected are:")
j = 1
for colour in colour_type:
    print("Color code for Room {0}: {1}".format(j,colour))
    j += 1
variable_cost = no_rooms * 120
total = base_cost + variable_cost
print(f"Your total cost is ${total}")



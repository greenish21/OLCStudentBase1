
# Task 2

# A teacher wants to record the favourite colours of students
# in a class.

# The following program allows the teacher to enter the name
# and favourite colour of each of the 10 students.
# You can assume that every student has a unique name.
#==========================================================
'''
num_students = 10

for x in range(num_students):
     student_name = input("Enter the student's name: ")
     colour = input("Enter the student's favourite colour: ")
'''
#==========================================================
# Open the file COLOURS.py

# 1 Edit the program to use a conditional loop that 
#  keeps asking again and again until the teacher chooses 
#  not to enter any more students and colors.
# Store all inputs as lower case.

# Suitable input messages must be used.
# Save your program.                                      [2]
#==========================================================
'''
while True:
    student_name = input("Enter the student's name: ").lower()
    colour = input("Enter the student's favourite colour: ").lower()
    choice = input("Do you wish to continue? ").lower()
    if choice == 'no':
        break
'''
#==========================================================
# 2 Copy and Paste the above program into this section.
#   Edit the above program to:
# - create an empty dictionary called favourite_colours;
# - store the student's name and favourite colour in favourite_colours.
#
# The student's name must be used as the key and the
# favourite colour must be used as the value.
#
# For example: {"john": "red", "mary": "yellow"}
# Save your program.                                      [1]
#==========================================================
'''
favourite_colours = {}
while True:
    student_name = input("Enter the student's name: ").lower()
    colour = input("Enter the student's favourite colour: ").lower()
    favourite_colours[student_name] = colour
    choice = input("Do you wish to continue? ").lower()
    if choice == 'no':
        break
'''
#==========================================================
# 3 Copy and Paste the above program into this section.
# Edit the program to display the name and number of students who
# have a specified favourite colour.

# The program must:
# - ask the teacher to enter a colour to search for (change the input to lower case);
# - search the values stored in favourite_colours; 
# - count the number of students who have the specified favourite colour;
# - output the colour and the number of students who have selected that colour.
# - output the names of all the students who have chosen that color.
# - print an appropriate message if none of the students choose that color.

# For example:
# assuming this is your dictionary 
#   {"james":"red","ethan":"blue","aiden":"red","chloe":"yellow",}

# Enter color to search: red
# 2 students like red.
# Students who like red:
#   james
#   aiden

# Suitable input and output messages must be used.
# Save your program.                                      [7]
#==========================================================
favourite_colours = {}
while True:
    student_name = input("Enter the student's name: ").lower()
    colour = input("Enter the student's favourite colour: ").lower()
    favourite_colours[student_name] = colour
    choice = input("Do you wish to continue? ").lower()
    if choice == 'no':
        break
colour_search = input("Enter the colour you would like to search for: ").lower()
count = 0
names = []
for name in favourite_colours:
    if favourite_colours[name] == colour_search:
        count += 1
        names.append(name)
if count > 0:
    print(f"{count} students like {colour_search}.")
    print(f"Students who like {colour_search}:")
else:
    print(f"Nobody likes {colour_search}")
for name in names:
    print(name)




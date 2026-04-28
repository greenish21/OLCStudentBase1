
# =========================================================
# FILE IO PRACTICE QUESTIONS
# Focus: open(), .read(), .readlines(), .write(), .writelines()
# Modes: "r", "w", "a"
# =========================================================
# r = read
# w = write
# a = append

# .write()
# .read()  # Reads content, stores as string
# .readline() # Reads only 1 line
# .readlines() # Reads contents of file, store each line as an item in list
# .writelines() # Function parameter is a list. Output each item in list to file
'''
with open("example.txt", "w") as file:
    # write something
    file.write("Text")
    # Important: If file exists, it will overwrite, if file does not exist, it will create
with open("example.txt", "r") as file:
    # write something
    content = file.read()
# print(content)
'''

# ---------------------------------------------------------
# Question 1
# Basic reading using "r" and .read()
#
# A text file q1_greeting.txt contains the text:
# Hello and welcome to Python File IO.
#
# Write a program to:
# 1. Open the file in read mode
# 2. Read the full contents using .read()
# 3. Display the contents on the screen
#
# Write your code below.
# ---------------------------------------------------------
'''
with open("q1_greeting.txt", "r") as file:
    content = file.read()
print(content)
'''
# ---------------------------------------------------------
# Question 2
# Basic writing using "w" and .write()
#
# Write a program to create a text file called q2_note.txt.
#
# The program should:
# 1. Open the file in write mode
# 2. Write the following text into the file:
#    Today I learnt how to write to a file.
# 3. Close the file
#
# After writing, open the file again in read mode
# and display its contents.
#
# Write your code below.
# ---------------------------------------------------------
'''
with open("q2_note.txt", "w") as file:
    file.write("Today I learnt how to write to a file.")
with open("q2_note.txt", "r") as file:
    content = file.read()
print(content)
'''

# ---------------------------------------------------------
# Question 3
# Appending using "a" and .write()
#
# A text file q3_diary.txt already contains:
# I went to school today.
#
# Write a program to:
# 1. Open the file in append mode
# 2. Add this new line at the end of the file (next line):
#    I also revised Python at night.
# 3. Close the file
# 4. Open the file again and display the full contents
#
# Write your code below.
# ---------------------------------------------------------
'''
with open("q3_diary.txt", "a") as file:
    file.write('\nI also revised Python at night.')
with open("q3_diary.txt", "r") as file:
    content = file.read()
print(content)
'''

# ---------------------------------------------------------
# Question 4
# Reading line by line using .readlines()
#
# A text file q4_fruits.txt contains:
# apple
# banana
# orange
# mango
#
# Write a program to:
# 1. Open the file in read mode
# 2. Read all lines using .readlines()
# 3. Display:
#    - the list of lines read from the file
#    - the total number of fruits in the file
#
# Write your code below.
# ---------------------------------------------------------
'''
with open("q4_fruits.txt", "r") as file:
    content = file.readlines()
print(f"The file has {len(content)} lines.")
print(f"The file has {len(content)} fruits.")
'''

# ---------------------------------------------------------
# Question 5
# Read, process, and count
#
# A text file q5_marks.txt contains one mark per line:
# 75
# 62
# 88
# 49
# 91
# 56
#
# Write a program to:
# 1. Read all the marks from the file
# 2. Convert them into integers
# 3. Find and display:
#    - the highest mark
#    - the lowest mark
#    - the average mark
# 4. Display how many students passed
#
# A pass is 50 or more.
#
# Write your code below.
# ---------------------------------------------------------
'''
with open("q5_marks.txt", "r") as file:
    content = file.readlines()
int_list = []
for num in content:
    num = num[:2]
    int_list.append(num)

print(int_list)
highest = max(int_list)
lowest = min(int_list)
total = sum(int(num) for num in int_list)
length = len(int_list)
average = total / length
pass_list = []
for num in int_list:
    num = int(num)
    if num >= 50:
        pass_list.append(num)


print(f"{highest} is the highest mark")
print(f"{lowest} is the lowest mark")
print(f"{average} is the average mark")
print(f"{len(pass_list)} is the number of poeple who passed")
'''






# ---------------------------------------------------------
# Question 6
# Read from one file, write to another
#
# A text file q6_names.txt contains:
# amir
# beth
# chen
# divya
#
# Write a program to:
# 1. Read all the names from q6_names.txt
# 2. Convert each name so that it starts with a capital letter
#    and the remaining letters are in lowercase
# 3. Write the updated names into a new file called proper_names.txt
#    with one name per line
#
# Example output in proper_names.txt:
# Amir
# Beth
# Chen
# Divya
#
# Write your code below.
# ---------------------------------------------------------
'''
with open("q6_names.txt", "r") as file:
    content = file.readlines()
with open("proper_names.txt", "a") as file2:    
    for name in content:
        name = name.strip()
        name = name[0:1].upper() + name[1:]
        file2.write(f"{name}\n")
'''
# ---------------------------------------------------------
# Question 7
# Filtering data
#
# A text file q7_temperatures.txt contains one temperature per line:
# 29
# 31
# 33
# 28
# 35
# 30
# 36
#
# Write a program to:
# 1. Read all temperatures from the file
# 2. Store only the temperatures greater than 30 in a list
# 3. Write these temperatures into a new file called hot_days.txt
#    with one value per line
# 4. Display how many hot days there are
#
# Write your code below.
# ---------------------------------------------------------
'''
with open("q7_temperatures.txt", "r") as file:
    content = file.readlines()
with open("hot_days.txt", "w") as file1:
    for temp in content:
        if int(temp[:2]) > 30:
            file1.write(temp)
with open("hot_days.txt", "r") as file2:
    content1 = file2.readlines()
    print(f"There are {len(content1)} hot days")       
'''                        

# ---------------------------------------------------------
# Question 8
# Matching two files into one result
#
# A text file q8_animal_names.txt stores a list of animals
# with a comma between each value.
#
# The current contents of q8_animal_names.txt are:
# cat,dog,rabbit,hamster
#
# A text file q8_animal_sounds.txt stores a list of animal sounds
# with a comma between each value.
#
# The current contents of q8_animal_sounds.txt are:
# meow,bark,squeak,peep
#
# Write a program to:
# 1. Read the data from both files
# 2. Split the values using the comma delimiter
# 3. Create a dictionary where:
#    - the animal is the key
#    - the sound is the value
# 4. Display the completed dictionary
#
# The program should work for files of any length.
# The files will always have the same number of values.
#
# Write your code below.
# ---------------------------------------------------------
'''
with open("q8_animal_names.txt", "r") as file_names:
    content_names = file_names.readline()
with open("q8_animal_sounds.txt", "r") as file_sounds:
    content_sounds = file_sounds.readline()
split_names = content_names.split(",")
split_sounds = content_sounds.split(",")

count = 0
animal_dict = {}
while count < len(split_names):
    animal_dict[split_names[count]] = split_sounds[count]
    count += 1
print(animal_dict)
'''

# ---------------------------------------------------------
# Question 9
# Validation and error reporting
#
# A text file q9_scores.txt contains one value per line:
# 56
# 72
# abc
# 91
# -4
# 105
# 68
#
# Write a program to read the file and check whether each line
# is a valid score.
#
# A valid score:
# - must be an integer
# - must be between 0 and 100 inclusive
#
# The program should:
# 1. Read all lines from the file
# 2. Separate the data into:
#    - valid scores
#    - invalid entries
# 3. Display both lists
# 4. Write all invalid entries into a file called invalid_scores.txt
#
# Note:
# Values such as abc, -4 and 105 are invalid.

# Write your code below.
# ---------------------------------------------------------
'''
with open("q9_scores.txt", "r") as file:
    content = file.readlines()
print(content)

valid = []
invalid = []

with open("invalid_scores.txt", "w") as file1:
    for score in content:
        score = score.strip()
        
        if score.isdigit():
            num = int(score)
            if 0 <= num <= 100:
                valid.append(num)
            else:
                invalid.append(score)
                file1.write(score + "\n")
        else:
            invalid.append(score)
            file1.write(score + "\n")
print(valid)
print(invalid)
'''

# ---------------------------------------------------------
# Question 10
# Summary report generation
#
# A text file q10_expenses.txt contains the following lines:
# Transport,12
# Food,8
# Books,15
# Transport,10
# Food,6
# Food,9
#
# Each line stores:
# category,amount
#
# Write a program to:
# 1. Read all lines from the file
# 2. Calculate the total amount spent
# 3. Calculate the total spent for each category
# 4. Write a report into a file called expense_report.txt
#
# The report should show:
# - total spending
# - total for Transport
# - total for Food
# - total for Books
#
# Example format:
# Total Spending: 60
# Transport: 22
# Food: 23
# Books: 15
# Write your code below.
# ---------------------------------------------------------
'''
with open("q10_expenses.txt", "r") as file:
    content = file.readlines()

list_split = []
for i in content:
    i = i.strip().split(",")
    list_split.append(i)

expense = {}
for item in list_split:
    if item[0] not in expense:
        expense[item[0]] = int(item[1])

    else:
        expense[item[0]] = expense[item[0]] + int(item[1])
total = sum(expense.values())
with open("expense_report.txt", "w") as f:
    f.write("Total Spending: " + str(total) + "\n")
    f.write("Transport: " + str(expense.get("Transport", 0)) + "\n")
    f.write("Food: " + str(expense.get("Food", 0)) + "\n")
    f.write("Books: " + str(expense.get("Books", 0)) + "\n")
'''
# ---------------------------------------------------------
# Question 11 [25 marks]
#
# A text file q11_sales.txt contains one sales record per line.
# Each line has the format:
# item_name,quantity,unit_price
#
# The current contents of q11_sales.txt are:
# Pen,12,1.5
# Book,5,4.8
# Eraser,20,0.6
# Pencil,10,1.2
# Ruler,3,2.5
#
# A program is required to read the sales data, process it,
# and write a report into a new text file called sales_report.txt.
#
# The report should contain:
# - the total value for each item
# - the grand total value of all items
# - the name of the item with the highest total value

# Write program code to perform this task.
# ---------------------------------------------------------
# You must use the following functions:
# (a) read_sales()                                         [5]
#     This function reads the data from q11_sales.txt.
#     It should return a nested list containing all sales records.
#     Each inner list should store:
#     - item name
#     - quantity as an integer
#     - unit price as a float
# Write your code below.
# ---------------------------------------------------------














# ---------------------------------------------------------
# (b) calculate_total(record)                              [4]
#     This function receives one sales record.
#     It should return the total value of that record.
#     total value = quantity x unit price
# Write your code below.
# ---------------------------------------------------------
















# ---------------------------------------------------------
# (c) write_report(records)                                [9]
#     This function receives the nested list of sales records.
#     It should:
#     - calculate the total value for each item
#     - calculate the grand total value
#     - determine the item with the highest total value (Best Selling Item)
#     - write the report into sales_report.txt

# Example contents of sales_report.txt:
# Pen: 18.0
# Book: 24.0
# Eraser: 12.0
# Pencil: 12.0
# Ruler: 7.5
# Grand Total: 73.5
# Best Selling Item: Book
#
# Write your code below.
# ---------------------------------------------------------












# ---------------------------------------------------------
# (d) Main program                                         [3]
#     The main program should:
#     - call read_sales()
#     - call write_report(records)
#     - display the message:
#       Report created successfully
#
# (e) Comments and meaningful variable names              [4]
#
# Write your code below.
# ---------------------------------------------------------
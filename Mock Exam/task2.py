
############################################################
# TASK 2 - REFINEMENT OF PROGRAM
############################################################

# The program allows a user to enter a word and stores the word in a list.
'''
word_list = []
word = input("Enter a word containing at least 5 letters: ")
word_list.append(word)
'''
#------------------------------------------------------------
# Task 2.1 [4]
#------------------------------------------------------------

# Extend the program so that the word entered is validated
# before it is stored in the list.
#
# The program must:
# - check that the word contains at least 5 characters;
# - check that every character in the word is an alphabetic letter;
# - if the word is invalid, output a suitable message explaining why and
#   repeatedly ask the user to enter another word until a
#   valid word is entered;
# - convert the valid word to lower case before storing it
#   into a list named word_list.
'''
word_list = []
while True:
    word = input("Enter a word containing at least 5 letters: ")
    if len(word) >= 5 and word.isalpha() == True:
        break
    else:
        if len(word) < 5:
            print("Length is invalid.")
        elif word.isalpha() == False:
            print("Word must have alphabetic letters only.")
word_list.append(word.lower())
'''
#------------------------------------------------------------
# Task 2.2 [5]
#------------------------------------------------------------

# Copy and paste your program from Task 2.1.
#
# Extend the program so that it:
# - asks the user whether another word is to be entered
#   after each valid word is stored;
# - accepts Y to enter another word and N to stop;
# - continues to apply the validation rules from Task 2.1
#   to every word entered;
# - stores every valid word in word_list;
# - outputs each word from the completed word_list one by one
#   when the user chooses to stop.
#
# You can assume that the user will only enter Y or N when asked
# whether another word is to be entered.
'''
word_list = []
while True:
    word = input("Enter a word containing at least 5 letters: ")
    if len(word) >= 5 and word.isalpha() == True:
        word_list.append(word.lower())
        stop = input("Do you wish to stop? (Y/N): ")
        if stop == "Y":
            break
    else:
        if len(word) < 5:
            print("Length is invalid.")
        elif word.isalpha() == False:
            print("Word must have alphabetic letters only.")
for i in word_list:
    print(i)
'''
#------------------------------------------------------------
# Task 2.3 [6]
#------------------------------------------------------------

# Copy and paste your program from Task 2.2.
#
# A dictionary is required to count the number of times each
# vowel occurs in all the words stored in word_list.
#
# Use the following dictionary:

vowel_count = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}
word_list = []
while True:
    word = input("Enter a word containing at least 5 letters: ")
    if len(word) >= 5 and word.isalpha() == True:
        word_list.append(word.lower())
        stop = input("Do you wish to stop? (Y/N): ")
        if stop == "Y":
            break
    else:
        if len(word) < 5:
            print("Length is invalid.")
        elif word.isalpha() == False:
            print("Word must have alphabetic letters only.")
for i in word_list:
    print(i)
for word in word_list:
    for char in word:
        if char == "a":
            vowel_count["a"] += 1
        elif char == "e":
            vowel_count["e"] += 1
        elif char == "i":
            vowel_count["i"] += 1
        elif char == "o":
            vowel_count["o"] += 1
        elif char == "u":
            vowel_count["u"] += 1    
print(vowel_count)   
for vowel in vowel_count:
    print(f"{vowel} occurs {vowel_count[vowel]} times")     
# Extend the program so that it:
# - checks every character in every word stored in word_list;
# - increases the correct value in vowel_count whenever a
#   vowel is found;
# - outputs the completed vowel_count dictionary;
# - outputs the count for each of the five vowels using
#   suitable output messages.




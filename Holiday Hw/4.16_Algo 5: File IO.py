
##############################################################
# Task: Sherlock Holmes – Vowel Counter
# Save your program as sherlockvowel.py
#
# You are hired to assist in analyzing the literary style of
# Arthur Conan Doyle. Your job is to write a program to analyze
# a text file called "308_sherlock.txt" (provided to you) and
# count the number of times each vowel appears.
#
# Then, your program should identify which vowel appears the most.
# After completing the analysis, write the results to a new file
# named "sherlockvowel.txt" with the following format:
#
# Example output format (numbers will vary):
# a : 37
# e : 98
# i : 56
# o : 88
# u : 66
#
# The most frequently appearing vowel is e
#
# ---------------------------------------------------------------
# What you need to do:
# 1. Open the file "308_sherlock.txt" and read its contents.
# 2. Count the number of times each vowel appears (a, e, i, o, u).
#    - Ignore case (i.e., 'A' and 'a' are the same).
# 3. Identify which vowel appears the most.
# 4. Create a new file called "sherlockvowel.txt".
# 5. Write the vowel counts and the most frequent vowel to the file.
# 6. You may use dictionaries or variables to store counts.
#
# Hints:
# - Use .lower() to convert all text to lowercase before counting.
# - You can use a dictionary like: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# - Use a loop to go through each character in the file.
# - Use the max in a list algo to find the most frequent vowel.
#
# Bonus: Print the results on the screen too (optional)    
##############################################################
with open("308_sherlock.txt", "r") as file:
    contents = file.read()

vowels = 0
for letter in contents.lower():
    if letter in "aeiou":
        vowels += 1
print(f"There are {vowels} vowels.")
#
a = 0
e = 0
i = 0
o = 0
u = 0

for letter in contents:
    if letter == "a":
        a += 1
    elif letter == "e":
        e += 1
    elif letter == "i":
        i += 1
    elif letter == "o":
        o += 1
    elif letter == "u":
        u += 1
max_vowel = "a"
max_count = a
if e > max_count:
    max_vowel = "e"
    max_count = e
if i > max_count:
    max_vowel = "i"
    max_count = i
if o > max_count:
    max_vowel = "o"
    max_count = o
if u > max_count:
    max_vowel = "u"
    max_count = u
print("Most common vowel:", max_vowel)
print("Count:", max_count)
'''
# Corrected Code
import random
questions = 10
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions):  # 11. Should not be minus 1 from questions
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer = num1 + num2 # 4. answer not defined
    print("What is", num1, "+", num2, "?")
    user_answer = int(input()) # 7. Input must convert to integer
    if user_answer == answer:
        if num1 > 25 and num2 > 25: # 9. Should be and condition
            total_mark = total_mark + 2
        else:
            total_mark = total_mark + 1
            answer_list = answer_list + ['Correct'] # 1. Fixed wrong quotation mark, # 8. Code was in the wrong place, out of if condition
    else:
        answer_list = answer_list + ["Incorrect"]

list_length = len(answer_list) # -1 # 2. Fixed wrong '-' sign, # 3. Fixed -1 list
for i in range(list_length):
    if answer_list[i] == "Correct": # 10. Should be i not x
        correct = correct + 1 # 6. Not adding correctly, changed to +
if correct  == 1: # 5. Message variable is wrong, replace with correct
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)'''




# Corrected Code

import random
questions = 10
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions): # 11. Removed -1
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer = num1 + num2 # 4. Fixed answer not defined
    print("What is", num1, "+", num2, "?")
    user_answer = int(input()) # 7. Changed input to integer
    if user_answer == answer:
        if num1 > 25 and num2 > 25: # Should be 'and' condition
            total_mark = total_mark + 2
        else:
            total_mark = total_mark + 1
            answer_list = answer_list + ['Correct'] # 1. Fixed wrong quotaation 8. Code in wrong place
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) # 2. Fixed wrong '-' 3. Fixed -1 List
for i in range(list_length):
    if answer_list[i] == "Correct": # 10. Should be i
        correct = correct + 1 # 6. Changed to plus as not adding correctly.
if correct  == 1: # 5. Message changed to correct
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)

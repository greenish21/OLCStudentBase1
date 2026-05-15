
###############################################################
# Scenario: Employee Performance Review

# Finding Maximum, Minimum, and Average Performance Scores 
# Without Built-in Functions
# YOU CANNOT USE ANY PYTHON INBUILT FUNCTIONS TO DO THIS.

# A company conducts annual performance reviews for employees. 
# Each employee is given a performance score out of 100. 
# The HR department wants to:

# - Identify the top-performing employee (highest score).
# - Identify the lowest-performing employee (lowest score).
# - Calculate the average performance score, rounded to 2 decimal places.
# - Identify underperforming employees (those with scores below 50) 
#    -> save them into another dictionary called non_performers.
#   and print a performance warning message to all of these employees.

performance_scores = {
    'Alice': 88, 'Benny': 75, 'Charlie': 92, 'David': 85,
    'Emma': 78, 'Farah': 81, 'George': 66, 'Hassan': 94,
    'Ivy': 71, 'Jack': 88, 'Liam': 45, 'Jessica': 98,
    'Samir': 23, 'Jimmy': 5, 'Bryan': 78, 'Estelle': 9}

# write your code here
max = 0
for key in performance_scores:
    value = int(performance_scores[key])
    if value > max:
        max = value
for key in performance_scores:
    if performance_scores[key] == max:
        print(f"The top performing employee is {key}")
#
min = 100
for key in performance_scores:
    value = int(performance_scores[key])
    if value < min:
        min = value
for key in performance_scores:
    if performance_scores[key] == min:
        print(f"The lowest performing employee is {key}")
#
total = 0
count = 0
for key in performance_scores:
    total += performance_scores[key]
    count += 1
average = total / count
print(f"The average performance score is {average:.2f}")
#
non_performers = {}
for key in performance_scores:
    value = int(performance_scores[key])
    if value < 50:
        non_performers[key] = value
name = input("Input your name: ")
if name in (non_performers):
    print("You are under performance")
else:
    print("You are performing well")
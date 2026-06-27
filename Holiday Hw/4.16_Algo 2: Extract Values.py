

##################################
# Assignment
# Scenario: Identifying Star Students for an Award Ceremony
    
# Your school is preparing for the end-of-year award ceremony.
# The principal wants to recognise "Star Students" — those who have shown:
# - Excellent attendance (at least 90%)
# - Strong academic performance (score of at least 85)

# You're given two separate dictionaries:
# - One with student attendance (in %)
# - One with student scores (out of 100)

# Extract the names of students who meet both criteria.
# (1) Store them in a list called star_students.
    
# (2) Loop through the star_students list and 
#      print a congratulatory message to each star student like this:
# "Congratulations Chloe Lim! With an attendance of 95% and a score of 92,
# you are awarded the Star Student Award!""

# You may assume that the same keys exist in both dictionaries.

attendance = {
    "Alex Tan": 92, "Benjamin Lee": 88, "Chloe Lim": 95,
    "Dana Ong": 87, "Ethan Raj": 91, "Farah Bte Ahmad": 94,
    "Gerald Chan": 78, "Hannah Goh": 85, "Ivan Wong": 96,
    "Jolene Ng": 93, "Kishore Menon": 70, "Liyana Yusof": 90
}

scores = {
    "Alex Tan": 84, "Benjamin Lee": 86, "Chloe Lim": 92,
    "Dana Ong": 81, "Ethan Raj": 89, "Farah Bte Ahmad": 90,
    "Gerald Chan": 65, "Hannah Goh": 88, "Ivan Wong": 93,
    "Jolene Ng": 79, "Kishore Menon": 72, "Liyana Yusof": 85
}
#
attendance_list = []
for key in attendance:
    value = attendance[key]
    if value >= 90:
        attendance_list.append(key)
scores_list = []
for key in scores:
    value = scores[key]
    if value >= 85:
        scores_list.append(key)
star_students = []
for i in attendance_list:
    if i in scores_list:
        star_students.append(i)
print(star_students)
for i in star_students:
    print(f"Congratulations {i}! With an attendance of {attendance[i]}% and a score of {scores[i]}, you are awarded the Star Student Award!")
  
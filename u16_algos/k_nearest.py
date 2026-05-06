
# Starter Question — Calculating Euclidean Distance for Plant Prediction
plant_records = {
    'P001': [8.2, 3.1, 'Herb'],
    'P002': [7.8, 2.9, 'Herb'],
    'P003': [21.5, 8.8, 'Shrub'],
    'P004': [23.2, 9.5, 'Shrub'],
    'P005': [45.0, 18.0, 'Tree'],
    'P006': [48.5, 19.2, 'Tree']
}

# Each record contains:
# plant_code: [leaf_length_cm, leaf_width_cm, plant_type]

#========================================================
# Task 1 [6]

# Write program code to predict the plant type of an unknown plant 
# using the nearest neighbour method.

# Your program should:
# - prompt the user to input the leaf length
# - prompt the user to input the leaf width
# - calculate the Euclidean distance between the unknown plant and each plant in plant_records
# - find the plant with the shortest distance
# - output the predicted plant type

# The Euclidean distance formula for two features is:

# import math
# distance = math.sqrt((new_length - existing_length) ** 2 + (new_width - existing_width) ** 2)

# Test your program using:
# leaf_length = 22.0
# leaf_width = 9.0
#--------------------------------------------------------
'''
import math

leaf_length = float(input("Enter leaf length: "))
leaf_width = float(input("Enter leaf width: "))

shortest_distance = 99999
predicted_type = ""

for plant_code in plant_records:
    plant = plant_records[plant_code]

    existing_length = plant[0]
    existing_width = plant[1]
    plant_type = plant[2]

    distance = math.sqrt((leaf_length - existing_length) ** 2 + (leaf_width - existing_width) ** 2)

    if distance < shortest_distance:
        shortest_distance = distance
        predicted_type = plant_type

print("Predicted plant type:", predicted_type)
'''



#########################################################
#########################################################
##########* * * * * * * Question 1 * * * * *#############
#########################################################
#########################################################

# Question 1 — Predicting Weather Type
day_ids = [
    'D001', 'D002', 'D003', 'D004', 'D005',
    'D006', 'D007', 'D008', 'D009', 'D010',
    'D011', 'D012', 'D013', 'D014', 'D015'
]

# Each item contains:
# [temperature, humidity, wind_speed, weather_type]
weather_data = [
    [32.1, 68, 10, 'Sunny'],
    [31.5, 72, 12, 'Sunny'],
    [33.0, 65, 8, 'Sunny'],
    [30.8, 74, 11, 'Sunny'],

    [25.2, 92, 21, 'Rainy'],
    [24.8, 95, 18, 'Rainy'],
    [26.0, 90, 20, 'Rainy'],
    [25.5, 88, 23, 'Rainy'],

    [28.2, 83, 22, 'Cloudy'],
    [27.8, 85, 24, 'Cloudy'],
    [29.0, 80, 19, 'Cloudy'],
    [28.5, 82, 21, 'Cloudy'],

    [30.0, 89, 28, 'Stormy'],
    [29.2, 91, 30, 'Stormy'],
    [30.5, 87, 27, 'Stormy']
]

#========================================================
# Task 1.1 [3]

# Write program code to create a dictionary named weather_records that uses 
# the values in day_ids as keys and their corresponding weather data as values.
#--------------------------------------------------------
weather_records = {}
count = 0
for day in day_ids:
    weather_records[day] = weather_data[count]
    count += 1
#========================================================
# Task 1.2 [2]
# Write program code to delete the record with day ID:
# 'D003'

# Then add the following new record:
# 'D016': [31.8, 70, 9, 'Sunny']
#--------------------------------------------------------
remove = weather_records.pop('D003')
weather_records['D016'] = [31.8, 70, 9, 'Sunny']
print(weather_records)
#========================================================
# Task 1.3 [8]
# Write program code to predict the weather_type for a new day 
# using the nearest neighbour method based on three features:

# temperature
# humidity
# wind_speed

# Your updated program should:
# - prompt the user to enter temperature
# - prompt the user to enter humidity
# - prompt the user to enter wind speed
# - calculate the Euclidean distance between the new day and every existing record
# - find the record with the shortest distance
# - output the nearest day ID
# - output the predicted weather type

# Test your program using:

# temperature = 29.5
# humidity = 88
# wind_speed = 27
#--------------------------------------------------------
import math

temp = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
wind_speed = float(input("Enter wind speed: "))

shortest_distance = 99999
predicted_type = ""
nearest_day = ""

for day in weather_records:
    record = weather_records[day]

    existing_temp = record[0]
    existing_humidity = record[1]
    existing_wind = record[2]
    weather_type = record[3]

    distance = math.sqrt(
        (temp - existing_temp) ** 2 +
        (humidity - existing_humidity) ** 2 +
        (wind_speed - existing_wind) ** 2
    )

    if distance < shortest_distance:
        shortest_distance = distance
        predicted_type = weather_type
        nearest_day = day

print("Nearest Day ID:", nearest_day)
print("Predicted Weather Type:", predicted_type)
#########################################################
#########################################################
##########* * * * * * * Question 2 * * * * *#############
#########################################################
#########################################################

# Question 2 — Predicting Type of Music
song_ids = [
    'S001', 'S002', 'S003', 'S004', 'S005',
    'S006', 'S007', 'S008', 'S009', 'S010',
    'S011', 'S012', 'S013', 'S014', 'S015'
]

# Each item contains:
# [title, tempo_bpm, loudness, duration_seconds, genre]
songs = [
    ['Fire Run', 145, 8.5, 210, 'Rock'],
    ['Night Drive', 138, 8.0, 225, 'Rock'],
    ['Thunder Road', 150, 8.8, 205, 'Rock'],
    ['Broken Strings', 142, 8.3, 230, 'Rock'],

    ['Blue Rain', 95, 4.2, 260, 'Jazz'],
    ['Moonlight Walk', 90, 3.8, 275, 'Jazz'],
    ['Late Cafe', 98, 4.5, 255, 'Jazz'],
    ['Smooth River', 88, 3.9, 290, 'Jazz'],

    ['Electric Jump', 128, 7.5, 200, 'Pop'],
    ['Summer Lights', 122, 7.0, 215, 'Pop'],
    ['City Dance', 126, 7.2, 205, 'Pop'],
    ['Bright Days', 118, 6.8, 220, 'Pop'],

    ['Golden Strings', 72, 3.2, 320, 'Classical'],
    ['Morning Sonata', 68, 3.0, 340, 'Classical'],
    ['Quiet Garden', 75, 3.4, 315, 'Classical']
]
#========================================================
# Task 2.1 [3]
# Write program code to create a dictionary named music_library 
# that uses song_ids as keys and the corresponding song details as values.
#--------------------------------------------------------




#========================================================
# Task 2.2 [4]

# Write a function named distance_2d() that accepts four parameters:
# x1, y1, x2, y2
# The function should return the Euclidean distance between the two points.

# The formula is:
# import math
# distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) 
#--------------------------------------------------------




#========================================================
# Task 2.3 [5]

# Write program code to predict the genre of a new song using 
# the nearest neighbour method based on two features:
# - tempo_bpm
# - loudness

# Your program should:

# - prompt the user to input the new song’s tempo
# - prompt the user to input the new song’s loudness
# - use distance_2d() to calculate the distance from each song
# - find the song with the shortest distance
# - output the predicted genre

# Test your program using:
# tempo_bpm = 126
# loudness = 7.2
#--------------------------------------------------------






#========================================================
# Task 2.4 [5]

# Edit your program from Task 2.3 so that it predicts the genre using three features:
# tempo_bpm
# loudness
# duration_seconds

# Your updated program should:

# prompt the user to enter tempo
# prompt the user to enter loudness
# prompt the user to enter duration
# calculate the Euclidean distance using all three features
# output the nearest song title
# output the predicted genre

# Test your program using:

# tempo_bpm = 73
# loudness = 3.3
# duration_seconds = 325
#--------------------------------------------------------





#########################################################
#########################################################
##########* * * * * * * Question 3 * * * * *#############
#########################################################
#########################################################
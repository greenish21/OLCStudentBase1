weather_data = [
    [30.0, 8.0, "No Rain"],
    [29.0, 12.0, "No Rain"],
    [27.0, 18.0, "Rain"],
    [25.0, 22.0, "Rain"],
    [32.0, 6.0, "No Rain"],
    [26.0, 16.0, "Rain"],
    [31.0, 10.0, "No Rain"],
    [28.0, 20.0, "Rain"]
]
# Task 4.1
def calculate_distance(temperature1,wind_speed1,temperature2,wind_speed2):
    temp_squared = (temperature1 - temperature2)**2
    wind_speed_squared = (wind_speed1 - wind_speed2)**2
    distance = (temp_squared + wind_speed_squared)**0.5
    return distance

# Task 4.2
def find_nearest(distance_list):
    smallest_dist = distance_list[0]
    for distance in distance_list:
        if distance < smallest_dist:
            smallest_dist = distance
    count = 0
    for dist in distance_list:
        if smallest_dist == dist:
            break
        else:
            count += 1
    return count
# Task 4.3
def predict_rain(current_temperature,current_wind_speed,weather_data):
    measurements = []
    for data in weather_data:
        dist = calculate_distance(current_temperature,current_wind_speed,data[0],data[1])
        measurements.append(dist)
    smallest_index = find_nearest(measurements)
    return weather_data[smallest_index][2]
# Task 4.4
prediction_records = []
while True:
    current_temperature = float(input("Enter your current temperature: "))
    current_wind_speed = float(input("Enter your current wind speed: "))
    prediction = predict_rain(current_temperature,current_wind_speed,weather_data)
    print(f"The predicted weather is {prediction}")
    prediction_records.append(f"{current_temperature},{current_wind_speed},{prediction}")
    start = input("Do you need another prediction? (Y/N): ")
    if start == "N":
        break
with open("weather_predictions.txt","w") as file:
    for data in prediction_records:
        file.write(f"{data}\n")


import math

#### do not change this code
devices = {
    "523WR": ["Telmo",  "Speed23",  "PMD",     0.70, 1.10],
    "924MN": ["Lambo",  "Comfit1",  "PMD",     0.60, 1.15],
    "32XC" : ["Lambo",  "Zipline",  "Scooter", 0.35, 0.60],
    "A101X": ["Volt",   "Feather",  "Scooter", 0.32, 0.52],
    "D404Q": ["RoadMax","Urban",    "PMD",     0.66, 1.18],
}

print("Mobility Device Classifier (kNN, k = 1)")
print("Total devices loaded:", len(devices))
#### do not change this code

# Task 2.1 - Complete the function below
def distance2(p1x, p1y, p2x, p2y):
    # Task 2.1 – To be completed by student
    return math.sqrt( (p1x - p2x)**2 + (p1y - p2y)**2 )

# Task 2.2 - Complete the function below
def predict_type_2d(devices_dict, newdevice_width, newdevice_length):
    # Task 2.2 – To be completed by student
    keys = []
    for device in devices_dict:
        keys.append(devices_dict[device])
        print(keys)
    smallest_dist = 99999
    closest_data = None
    for data in keys:
        width = data[3]
        length = data[4]
        distance = distance2(width, newdevice_width, length, newdevice_length)
        if distance < smallest_dist:
            smallest_dist = distance
            closest_data = data
    return closest_data[2]
print(predict_type_2d(devices, 2, 3))


# --- main flow (to be refined by you) ---
# Students will add input validation and output formatting later

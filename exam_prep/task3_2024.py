flag = False
while flag:
    length = float(input("What is the length of the parcel?"))
    width = float(input("What is the width of the parcel?"))
    depth = float(input("What is the depth of the parcel?"))
    if length > 50 and length > 50 and depth > 50:
        parcel_size = "large"
    elif length > 50 and width > 50 or depth > 50:
        parcel_size = "medium"
    elif:
        parcel_size = "small"
    more_parcels = input("Do you want to enter another parcel? Y or N ")
    if more_parcels = N:
        flag = True
print("The size of your parcel is", more_parcels)
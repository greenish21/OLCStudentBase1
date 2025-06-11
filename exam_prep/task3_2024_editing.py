flag = True # 5. Flag must be true
while flag:
    length = int(input("What is the length of the parcel? ")) # 8. Changed float to int
    width = int(input("What is the width of the parcel? "))
    depth = int(input("What is the depth of the parcel? "))
    more_parcels = input("Do you want to enter another parcel? Y or N ").upper # 3. Changed position # 10. Upper
    if length > 50 and width > 50 and depth > 50: # 6. Removed 1 length
        parcel_size = "large"
    elif length > 50 and width > 50 and depth <= 50: # 7. Changed or to and # 8. depth <= 50
        parcel_size = "medium"
    else:
        parcel_size = "small" # 1. Changed elif to else
        
    if more_parcels == 'N': # 2. Changed N to string # 9. Should be ==
        flag = False
        break
    print("The size of your parcel is", parcel_size) # 4. Changed more parcels to parcel size # 10. Indent
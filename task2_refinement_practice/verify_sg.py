# Task 2
'''
ID = ""
for i in range(2):
    ID = input("Enter ID: ")
    if ID[0] == "S":
        print("Welcome home!")
    else:
        print("Welcome to Singapore!")
'''
      
# Task 2.1
'''
count = 0
for i in range(5):
    ID = input("Enter ID: ").upper()
    if ID[0] == "S" or ID[0] == "T":
        print("Welcome home!")
        count += 1
    else:
        print("Welcome to Singapore!")
print(f"There are {count} Singaporeans")
'''
# Task 2.2
count = 0

while True:
    ID = input("Enter ID (or 'q' to quit): ")
    
    if ID.lower() == 'q':
        break
    
    if len(ID) != 9:
        print("Invalid, ID must be 9 characters long")
    else:
        if ID[0] == "S" or ID[0] == "T":
            print("Welcome home!")
            count += 1
        else:
            print("Welcome to Singapore!")

print(f"There are {count} Singaporeans")
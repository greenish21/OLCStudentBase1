sports_list = []
while True:
    sport = input("What is the member's preferred sport? ")
    if sport.lower() == "done":
        break
    else:
        sports_list.append(sport.lower())

search = input("What sport would you like to search for? ").lower()
if search not in sports_list:
    print(f"Nobody likes {search}")
else:
    count_list = sports_list.count(search)
    print(f"{count_list} people like {search}")

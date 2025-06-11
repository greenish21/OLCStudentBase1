### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this

if action == "b" or action == "B": # 1. Changed = to == and added : # 7. Added capital letter
    if books[book_id] == "AVAILABLE": # 9. Change AVALIABLE
        books[book_id] = "BORROWED" # 10. Change book_id and BORROWED
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action == "r" or action == "R": # 2. Changed = to == # 8. Added capital letter
    if books[book_id] == "BORROWED":
        books[book_id] = "AVAILABLE" # 3. Changed round bracket to square bracket
        print("You have returned the book.") # 4. Added missing quotation mark
    else: # 6. Changed else to elif
        print("The book is already available.") # 5. Added missing indent
else:
    print("Invalid action")
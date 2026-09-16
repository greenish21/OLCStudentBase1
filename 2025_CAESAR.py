# Task 5.1
def shift(char):
    ascii_char = ord(char)
    shift_ascii = ascii_char + 1
    shifted = chr(shift_ascii)
    if char == "z":
        return "a"
    else:
        return shifted
# Task 5.2
def encrypt(message, positions):
    encrypted = message
    count = 0
    while count < positions:
        temp_encrypted = ""
        for char in encrypted:
            temp_encrypted += shift(char)
        encrypted = temp_encrypted
        count += 1
    return encrypted
# Task 5.3
def shift_up(char):
    ascii_char = ord(char)
    shift_ascii = ascii_char - 1
    shifted = chr(shift_ascii)
    if char == "a":
        return "z"
    else:
        return shifted
# Task 5.4
def decrypt(ciphertext, positions):
    decrypted = ciphertext
    count = 0
    while count < positions:
        temp_decrypted = ""
        for char in decrypted:
            temp_decrypted += shift_up(char)
        decrypted = temp_decrypted
        count += 1
    return decrypted
# Task 5.5
while True:
    choice = input("Enter ‘E’ to encrypt a message or ‘D’ to decrypt a ciphertext: ").upper()
    if choice == "E" or choice == "D":
        break
    else:
        print("Invalid choice. Please reenter: ")
if choice == "E":
    message = input("Enter your message: ")
elif choice == "D":
    ciphertext = input("Enter your ciphertext: ")
while True:
    positions = int(input("Enter the number of positions to shift the letters: "))
    if str(positions).isdigit() == True and positions > 0:
        break
    else:
        print("Invalid position. Please reenter: ")
if choice == "E":
    encrypted = encrypt(message, positions)
    print(f"The encrypted message is {encrypted}.")
    with open("encrypted.txt","w") as file:
        file.write(encrypted)
elif choice == "D":
    decrypted = decrypt(ciphertext, positions)
    print(f"The decrypted message is {decrypted}.")

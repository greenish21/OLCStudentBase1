# Task 5.1
def shift(char):
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    if char in alphas:
        index = alphas.find(char)
        shifted_index = (index + 1) % 26

        return alphas[shifted_index]
    else:
        return char
    
# Task 5.2
def encrypt(message, positions):
    encrypted = ''
    for c in message:
        char = c
        for i in range(positions):
            char = shift(char)
        encrypted = encrypted + char
    return encrypted

# Task 5.3
def shift_up(char):
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    if char in alphas:
        index = alphas.find(char)
        shifted_index = (index - 1)%26
        return alphas[shifted_index]
    else:
        return char
    
# Task 5.4
def decrypt(message, positions):
    decrypted = ''
    for c in message:
        char = c
        for i in range(positions):
            char = shift_up(char)
        decrypted = decrypted + char
    return decrypted

# Task 5.5
while True:
    command = input("Type E/e to encrypt, or D/d to decrypt: ").lower()
    if command not in "de":
        print("Invalid input. Only E/e or D/d.")
    else:
        break
if command == "e":
    content = input("Input message for encryption: ")
elif command == "d":
    content = input("Input ciphertext for decryption: ")

while True:
    shiftnum = input("Enter positions to shift: ")
    if shiftnum.isdigit() and int(shiftnum) > 0:
        shiftnum = int(shiftnum)
        break
    else:
        print("Shift position must be a positive integer")

if command == 'e':
    encrypted = encrypt(content, shiftnum)
    print(f"Encrypted text is: {encrypted}")
    with open('encrypted.txt', 'w') as fobj:
        fobj.write(encrypted)

if command == 'd':
    decrypted = decrypt(content, shiftnum)
    print(f"Decrypted Test is: {decrypted}")
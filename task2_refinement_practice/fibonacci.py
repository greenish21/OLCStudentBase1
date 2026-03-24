# Task 2
'''
n1 = 0
n2 = 1
nterms = 5
for i in range(nterms):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
'''
# 6.
'''
n1 = 0
n2 = 1
nterms = input("Enter the number of terms you would like to enter: ")
for i in range(nterms):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
'''
# 7.
'''
n1 = 0
n2 = 1
while True:
    nterms = int(input("Enter the number of terms you would like to enter: "))
    if nterms <= 0:
        print("Incorrect term range")
    else:
        for i in range(nterms):
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
        break
'''
#8.
'''
sequence = []
n1 = 0
n2 = 1
while True:
    nterms = int(input("Enter the number of terms you would like to enter: "))
    if nterms <= 0:
        print("Incorrect term range")
    else:
        for i in range(nterms):
            print(n1)
            sequence.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
        break
print(sequence)
'''
# 9.
sequence = []
n1 = 0
n2 = 1
while True:
    nterms = int(input("Enter the number of terms you would like to enter: "))
    if nterms <= 0:
        print("Incorrect term range")
    else:
        for i in range(nterms):
            print(n1)
            sequence.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
        break
num = int(input("Enter another positive integer: "))
if num in sequence[0:100]:
    print("Your number is in the first 100th terms of the sequence.")
else:
    print("Your number is not in the first 100th terms of the sequence.")
print(sequence)
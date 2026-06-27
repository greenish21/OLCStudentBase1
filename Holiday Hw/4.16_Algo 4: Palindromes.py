
###########################################################
# Scenario 3: Secret Palindrome Message Checker (with Sentences)

# A group of friends is hiding palindromes in sentences 
# (ignoring punctuation, spacing, and casing). 
# You are building a tool to check if a sentence is a secret palindrome.

# For each sentence:
# (1) Remove spaces
# (2) Remove punctuation
# (3) Convert to lowercase
# (4) Check if it is a palindrome
# (5) Add all the original sentences that is a palindrome to a new list

sentences = [
    "A man a plan a canal Panama", "Was it a car or a cat I saw", "No lemon no melon",
    "Never odd or even", "Do geese see God", "Step on no pets", "Eva can I see bees in a cave",
    "Madam in Eden I m Adam", "Mr Owl ate my metal worm", "Go hang a salami Im a lasagna hog",
    "This is not a drill", "Hello world", "Random sentence",
    "My gym", "Yo banana boy", "Red roses run no risk sir on nurses order",
    "Borrow or rob", "Sir I demand I am a maid named Iris", "Too hot to hoot",
    "Do nine men interpret nine men I nod", "Not a palindrome", "Wow", "I saw I was I",
    "I did did I", "Dont nod", "Was it a rat I saw", "Murder for a jar of red rum",
    "Ma is as selfless as I am", "No x in Nixon", "Rats live on no evil star",
    "The sun sets in the west", "I love learning Python", "We are going to the mall later",
    "He forgot to bring his charger", "This assignment is due tomorrow", "I enjoy playing football",
    "She painted a beautiful sunset", "My favourite drink is iced lemon tea",
    "The teacher explained the topic clearly", "We had nasi lemak for breakfast",
    "There is a red car in the carpark", "It is raining heavily outside",
    "I need to complete my homework", "My friend just got a new phone",
    "The concert tickets were sold out", "They went hiking in the forest",
    "Please close the windows before you leave", "The robot stopped working after lunch",
    "We watched a movie last weekend", "Our team won the interclass tournament"
]
# write your code here
palindromes = []
for sentence in sentences:
    cleaned = ""
    for char in sentence:
        if char.isalnum():
            cleaned += char.lower()
    if cleaned == cleaned[::-1]:
        palindromes.append(sentence)
print(palindromes)



###########################################################
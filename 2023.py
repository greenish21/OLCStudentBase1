def split_sentence(word_string):
    list_sentence = word_string.split()
    return list_sentence

# Qn 10
def check_list(word,word_string):
    list_sentence = split_sentence(word_string)
    if word in list_sentence: # Checks if word is in list
        return "Yes"
    else:
        return "No"

# Qn 11
def reverse_sentence(word_string):
    list_sentence = split_sentence(word_string)
    reverse_list = []
    len_list = len(list_sentence)
    count = len_list
    while count > 0: 
        reverse_list.append(list_sentence[count-1]) # Adds words into the reverse list starting from the back
        count -= 1
    reverse_str = ""
    for i in reverse_list: # Converts list to string
        reverse_str = reverse_str + i + " "
    return reverse_str
print(reverse_sentence("the cat sat on the mat"))

# Qn 12
words_str = str(input("Enter your string of words: "))
word_search = str(input("Enter the word you would like to search: "))
word_list = split_sentence(words_str)
print(f"Your list of words is: {word_list}")
print(f"Your string reversed is: {reverse_sentence(words_str)}")
search = check_list(word_search,words_str)
if search == "Yes":
    print("Your word is found.")
else:
    print("Your word is not found.")
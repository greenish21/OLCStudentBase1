'''
Task 4 - 2023 Paper - Development of Program
Open the file SPLIT_SENTENCE.py. You will see the following function that 
takes a string of words, passed as the parameter word_string, splits it 
into individual words and stores these words in a list. 
It returns the list of words. 

You can assume the string does not contain punctuation marks.
'''
def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence

# Task 4.1 
def checklist(word, sentence):
    sentencelist = split_sentence(sentence)
    if word in sentencelist:
        return "Yes"
    else:
        return "No"
# Task 4.2
def reverse_sentence(sentence):
    sentence_list = split_sentence(sentence)
    list_reversed = []
    for i in sentence_list:
        list_reversed.insert(0, i)
        output = ""
        for item in list_reversed:
            output = output + item + ' '
        output = output.strip()
        return output
print(reverse_sentence("the cat sat on the mat"))

# Task 4.3
sentence = input("What is your sentence? ")
word = input("What is your word? ")

listsentence = split_sentence(sentence)
print(listsentence)

reversed = reverse_sentence(sentence)
print(reversed)

output = checklist(word, sentence)
if output == "Yes":
    print(f"The word {word} is in {sentence}")
if output == "No":
    print(f"The word {word} is not in {sentence}")


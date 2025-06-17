def CompareWords(word1,word2):
    longerword = ""
    shorterword = ""
    if len(word1) > len(word2):
        longerword = word1
        shorterword = word2
    elif len(word2) > len(word1):
        longerword = word2
        shorterword = word1
    else:
        print("Both words have the same length.")
    
    for char in longerword:
        if char not in shorterword:
            print(f"{char} is not in {shorterword}. ")

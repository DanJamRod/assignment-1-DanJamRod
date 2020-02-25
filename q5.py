def awesome_word(word):
    """ Finds if word is an awesome word (at least one identical non-overlapping word couplet and one xyx type substring)
    """
    flag = False
    for i in range (len(word)-2):
        for j in range (len(word)-3-i): # Searches if the two letters i and i+1 are found in the rest of the word. zzz returns false as the search starts at i+2 and i+3, not i+1 and i+2
            if word[i:i+2] == word[j+i+2:j+i+4]:
                flag = True
    if flag == False:
        return False

    flag = False
    for i in range(len(word)-2):
        if word[i] == word [i+2]:
            flag = True
    return flag

def find_awesome_words():
    """
    return the number of awesome words in the text file
    """
    f = open("drunkard_words.txt")
    count = 0
    for word in f:
        if awesome_word(word) == True:
            count += 1
    return count

print(find_awesome_words())
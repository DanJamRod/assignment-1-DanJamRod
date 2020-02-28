def good_word(word):
    """ Finds if word is a good word (vowels>=3, 1 double letter, no "ab" or "cd" or "xy")
    """
    count = 0
    for i in range (len(word)): # Count number of vowels, if >=3 program continues, otherwise return False
        if word[i] in "aoeiu":
            count += 1
    if count < 3:
        return False
    
    flag = False
    for i in range (len(word)-1): # If there is a double letter, flag will be True and program continues, otherwise return False
        if word[i] == word[i+1]:
            flag = True
    if flag == False:
        return False

    for i in range (len(word)-1): # If there is an ab, cd, or xy, flag will be False and program will return False, otherwise return True
        if word[i] + word[i+1] == "ab" or word[i] + word[i+1] == "cd" or word[i] + word[i+1] == "xy":
            flag = False
    return flag
    
def find_good_words():
    """
    return the number of good words in the text file
    """
    f = open("drunkard_words.txt")
    count = 0
    for word in f:
        if good_word(word) == True:
            print(word)
            count += 1
    return count

print(find_good_words())
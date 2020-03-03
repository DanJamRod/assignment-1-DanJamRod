def awesome_word(word):
    """ Finds if word is an awesome word (at least one identical non-overlapping word couplet and one xyx type substring)
    """
    flag = False # Sets flag initially to False
    for i in range (len(word)-2): # Runs the program for every letter except the last two (last two letters have no pairs to compare it to after)
        for j in range (len(word)-3-i): # Runs the program for every letter after letter[i]&[i+1], except the last two (last two letters have no pairs to compare it to after)
            if word[i:i+2] == word[j+i+2:j+i+4]: # Checks whether a specific letter pair is equal to a specific later pair
                flag = True # If there is an identical non-overlapping word couplet, flag changes to True
    if flag == False: # If the flag is not True, there is no identical non-overlapping word couplet, word is not awesome and returns False. If flag is True, word continues to the next check
        return False

    flag = False # Resets flag to False
    for i in range(len(word)-2): # Runs the program for every letter except the last two (last two letters have no letters to compare it to after)
        if word[i] == word [i+2]: # Checks whether the letter is the same as the second letter after (i.e. whether xyx, y can be any value(including x))
            flag = True # If there is an identical xyx type substring, flag changes to True
    return flag # If flag is False, no identical xyx type substring, word returns False. If identical xyx type substring, word is awesome so returns True

def find_awesome_words():
    """
    return the number of awesome words in the text file
    """
    f = open("drunkard_words.txt") # makes f notate the file "drunkard_words.txt"
    count = 0 # Start count at 0
    for word in f: # Runs program for every word in the list
        if awesome_word(word) == True: # Checks whether the word is an awesome word
            print(word) # Prints the word if it is an awesome word
            count += 1 # Adds 1 to the count if the word is an awesome word
    return count # After checking all of the words, returns the count of how many are good words

print(find_awesome_words())
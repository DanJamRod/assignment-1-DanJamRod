def good_word(word):
    """ Finds if word is a good word (vowels>=3, 1 double letter, no "ab" or "cd" or "xy")
    """
    count = 0 # Starts count at 0
    for i in range (len(word)): # Runs the program for every letter in word
        if word[i] in "aoeiu": # Checks whether letter is a vowel
            count += 1 # If letter is a vowel, adds 1 to count
    if count < 3: # If fewer than 3 vowels, ends program. If more, word continues to next check
        return False
    
    flag = False # Sets flag to "False" as default
    for i in range (len(word)-1): # Runs the program for every letter except the last (last letter has nothing to compare it to after)
        if word[i] == word[i+1]: # Checks whether letter is the same as the next letter
            flag = True # If the letter is the same, flag changes to True
    if flag == False: # If no double letter, flag is false, ends program. If double letter, flag is true, word continues to next check
        return False

    for i in range (len(word)-1): # Runs the program for every letter except the last (last letter has no letter after to pair with) 
        if word[i] + word[i+1] == "ab" or word[i] + word[i+1] == "cd" or word[i] + word[i+1] == "xy": # Checks whether the letter and the next letter together are "ab", "cd", or "xy"
            flag = False # If a letter pair is "ab", "cd", or "xy", flag changes to False. If none match, flag stays True
    return flag # Returns outcome of the last check
    
def find_good_words():
    """
    return the number of good words in the text file
    """
    f = open("drunkard_words.txt") # makes f notate the file "drunkard_words.txt"
    count = 0 # Start count at 0
    for word in f: # Runs program for every word in the list
        if good_word(word) == True: # Checks whether the word is a good word
            print(word) # Prints the word if it is a good word
            count += 1 # Adds 1 to the count if the word is a good word
    return count # After checking all of the words, returns the count of how many are good words

print(find_good_words())
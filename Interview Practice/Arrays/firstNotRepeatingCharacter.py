
# Use dictionary to get count of each occurance of a letter in the string
# If letter is not in dictionary
#   Put letter in dictionary with initial value of 1
# Else if letter is in dictionary
#   add 1 to the value of the key
# Check all keys and find first instance where key returns value of 1
#   If true, return the letter
# End of loop, return '_'
def firstNotRepeatingCharacter(s):
    charDictionary = {}
    strSplit = list(s)
    firstCharacter = ''
    for letter in strSplit:
        if letter in charDictionary:
            charDictionary[letter] += 1
        else:
            charDictionary[letter] = 1
            
    for letter in strSplit:
        if charDictionary[letter] == 1:
            return letter
    return '_'

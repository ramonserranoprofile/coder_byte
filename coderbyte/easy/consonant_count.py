"""
Consonant Count
Have the function ConsonantCount(str) take the str string parameter being passed and return the number of consonants the string contains.

Examples
Input: "Hello World"
Output: 7

Input: "Alphabets"
Output: 6 
"""

import re

def ConsonantCount(strParam):
    # code goes here
    vowels = 0
    consonants = 0

    strParam = re.sub("[^a-zA-Z]", "", strParam)
    print(strParam)

    for i in strParam:
        if (
            i == "a"
            or i == "e"
            or i == "i"
            or i == "o"
            or i == "u"
            or i == "A"
            or i == "E"
            or i == "I"
            or i == "O"
            or i == "U"
        ):
            vowels += 1
        else:
            consonants += 1
    return consonants

# keep this function call here
print(ConsonantCount(str(input())))

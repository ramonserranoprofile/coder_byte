# Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter
# is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. The parameter
# entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome.
# For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.

import string

def PalindromeTwo(strParam):
    punctuation = string.punctuation
    no_spaces_string = strParam.replace(" ", "").lower()
    no_punct_string = ''

    for char in no_spaces_string:
        if char in punctuation:
            continue
        else:
            no_punct_string += char

    return no_punct_string == no_punct_string[::-1]

# keep this function call here
print(PalindromeTwo(input("Input string: ")))
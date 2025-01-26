# First Reverse
# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.
# Examples
# Input: "coderbyte"
# Output: etybredoc
# Input: "I Love Code"
# Output: edoC evoL I


def FirstReverse(strParam):
    reversed_string = ""
    for char in strParam[::-1]:
        reversed_string += char
    return reversed_string


# keep this function call here
print(FirstReverse(input()))

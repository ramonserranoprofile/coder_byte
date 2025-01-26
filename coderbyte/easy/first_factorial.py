# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it
#(ie. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18.
# Use the Parameter Testing feature in the box below to test your code with different arguments.
# Codeland Username Validation
# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

# If the username is valid then your program should return the string true, otherwise return the string false.
# Examples
# Input: "aa_"
# Output: false
# Input: "u__hello_world123"
# Output: true

def FirstFactorial(num):
    if num == 0:
        return 1
    else:
        return FirstFactorial(num - 1) * num


# keep this function call here
# to see how to enter arguments in Python scroll down
print (FirstFactorial(int(input())))
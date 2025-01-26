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


def CodelandUsernameValidation(strParam):

    str_len = len(strParam)
    invalid_str_msg, valid_str_msg = "false", "true"

    # Rule 1
    if not ((str_len >= 4) and (str_len <= 25)):
        return invalid_str_msg

    # Rule 2
    if not strParam[0].isalpha():
        return invalid_str_msg

    # Rule 4
    if strParam.endswith("_"):
        return invalid_str_msg

    # Rule 3
    for ch in strParam:
        if (not ch.isalnum()) and (ch != "_"):
            return invalid_str_msg

    # Made it to the end so string must be valid
    return valid_str_msg


# keep this function call here
print(CodelandUsernameValidation(input()))

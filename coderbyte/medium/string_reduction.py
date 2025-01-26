# Example
# Input: "abcabc"
# Output: 2
# Input: "cccc"
# Output: 4
# Input: "abc"
# Output: 2

# Given a string of lowercase letters, you need to figure out the following operation:
# Find the smallest character in the string and replace all its occurrences with the second smallest character.
# Then find the smallest character in the string and replace all its occurrences with the second smallest character, and so on.
# Keep repeating this operation until there is only one distinct character left.
# Return the length of the final string.

# Solution
def StringReduction(str):
    str = list(str)
    cSet = set(["a", "b", "c"])
    repeat = True
    while repeat:
        i = 0
        repeat = False
        while i < len(str) - 1:
            if str[i] != str[i + 1]:
                str[i : i + 2] = list(cSet - set([str[i], str[i + 1]]))
                repeat = True
            else:
                i += 1
    return len(str)


# keep this function call here
# to see how to enter arguments in Python scroll down
print(StringReduction(input()))

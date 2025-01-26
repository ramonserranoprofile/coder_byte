# Swap Case
# Have the function SwapCase(str) take the str parameter and swap the case of each character. For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are.

# Examples
# Input: "Hello-LOL"
# Output: hELLO-lol
# Input: "Sup DUDE!!?"
# Output: sUP dude!!?

# Tags
# string manipulation

def SwapCase(str):
    return "".join([i.lower() if i.isupper() else i.upper() for i in str])


# keep this function call here
# to see how to enter arguments in Python scroll down
print(SwapCase(str(input())))

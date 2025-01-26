# Swap II
# Medium
# Have the function SwapII(str) take the str parameter and swap the case of each character. Then, if a letter is between two numbers, switch the places of the two numbers. For example: if str is "6Hello4 -8World, 7 yes3" the output should be 4hELLO6 -8wORLD, 7 YES3.
# Examples
# Input: "Hello -5LOL6"
# Output: hELLO -6lol5
# Input: "2S 6 du5d4e"
# Output: 2s 6 DU4D5E

# Tags
# string manipulation


def SwapII(str):
    result = [i.lower() if i.isupper() else i.upper() for i in str]
    first = -1
    for i in range(len(result)):
        if result[i].isdigit():
            if first == -1:
                first = i
            else:
                result[first], result[i] = result[i], result[first]
                first = -1
    return "".join(result)


# keep this function call here
print(SwapII(input()))

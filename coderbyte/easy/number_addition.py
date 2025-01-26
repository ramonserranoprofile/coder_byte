# Number Addition
# Have the function NumberAddition(str) take the str parameter, search for all the numbers in the string, add them together, then return that final number. For example: if str is "88Hello 3World!" the output should be 91. You will have to differentiate between single digit numbers and multiple digit numbers like in the example above. So "55Hello" and "5Hello 5" should return two different answers. Each string will contain at least one letter or symbol.
# Examples
# Input: "75Number9"
# Output: 84
# Input: "10 2One Number*1*"
# Output: 13
# Tags
# string manipulation


def NumberAddition(str):
    mark = 0
    result = 0
    for i in range(1, len(str) + 1):
        if not str[mark:i].isdigit():
            if mark + 1 != i:
                result += int(str[mark : i - 1])
            mark = i
    if str[mark:i].isdigit():
        result += int(str[mark:])
    return result


# keep this function call here
# to see how to enter arguments in Python scroll down
print(NumberAddition(input()))

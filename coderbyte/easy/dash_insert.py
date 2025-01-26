# Dash Insert
# Have the function DashInsert(num) insert dashes ('-') between each two odd numbers in num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
# Examples
# Input: 99946
# Output: 9-9-946
# Input: 56730
# Output: 567-30
# Tags
# string manipulationmath fundamentals


def DashInsert(num):
    result = ""
    for i in str(num):
        if len(result) == 0:
            result += i
            continue
        if int(i) % 2 == 1 and int(result[-1]) % 2 == 1:
            result += "-" + i
        else:
            result += i
    return result


# keep this function call here
# to see how to enter arguments in Python scroll down

print(DashInsert(int(input())))


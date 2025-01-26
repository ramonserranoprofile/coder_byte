# Countning Minutes I
# Have the function CountingMinutesI(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.
# Examples
# Input: "12:30pm-12:00am"
# Output: 690
# Input: "1:23am-1:08am"
# Output: 1425
# Tags
# string manipulationmath fundamentalssearching


def turn24H(time):
    result = time[:-2].split(":")
    result = (
        [int(result[0]), int(result[1])]
        if time[-2:] == "am"
        else [int(result[0]) + 12, int(result[1])]
    )
    result[0] = result[0] if (result[0] != 12 and result[0] != 24) else result[0] - 12
    return result

def CountingMinutesI(str):
    time1, time2 = [turn24H(time) for time in str.split("-")]
    if time1[0] <= time2[0]:
        return 60 * (time2[0] - time1[0]) + time2[1] - time1[1]
    else:
        return 60 * (24 - time1[0] + time2[0]) - time1[1] + time2[1]


# keep this function call here
# to see how to enter arguments in Python scroll down
# print(CountingMinutesI(input("Input 2 times in String(eg. 1:00pm-11:00am): "))) # 1:00pm-11:00am
print(CountingMinutesI("12:30pm-12:00am")) # 690
print(CountingMinutesI("1:00pm-11:00am"))  # 1320

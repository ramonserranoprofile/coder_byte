# Using the Python language, have the function CountingMinutes(str) take the str parameter being passed which will be
# two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of
# minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am
# then the output should be 60. If str is 1:00pm-11:00am the output should be 1320.


def CountingMinutes(a_string):
    times = a_string.split("-")
    two_times = []

    for time in times:
        split_time = time.split(":")
        hours = int(split_time[0])
        minutes = int(split_time[1][:2])

        if time[-2:] == "pm":
            hours += 12
        time_in_minutes = hours * 60 + minutes
        two_times.append(time_in_minutes)

    if times[0][-2:] == "pm" and times[1][-2:] == "am":
        return (1440 - two_times[0]) + two_times[1]
    elif two_times[0] < two_times[1]:
        return two_times[1] - two_times[0]
    else:
        return 1440 - (two_times[0] - two_times[1])


# keep this function call here
# to see how to enter arguments in Python scroll down
print(CountingMinutes(input("Input 2 times in String(eg. 1:00pm-11:00am): ")))

# Most Free Time
# Have the function MostFreeTime(strArr) read the strArr parameter being passed which will represent a full day and will be filled with events that span from time X to time Y in the day. The format of each event will be hh:mmAM/PM-hh:mmAM/PM. For example, strArr may be ["10:00AM-12:30PM","02:00PM-02:45PM","09:10AM-09:50AM"]. Your program will have to output the longest amount of free time available between the start of your first event and the end of your last event in the format: hh:mm. The start event should be the earliest event in the day and the latest event should be the latest event in the day. The output for the previous input would therefore be 01:30 (with the earliest event in the day starting at 09:10AM and the latest event ending at 02:45PM). The input will contain at least 3 events and the events may be out of order.

# Examples
# Input: ["10:00AM-12:30PM", "02:00PM-02:45PM", "09:10AM-09:50AM"]
# Output: 01:30
# Input: ["12:15PM-02:00PM", "09:00AM-10:00AM", "10:30AM-12:00PM"]
# Output: 00:30
# Input: ["12:15PM-02:00PM", "09:00AM-12:11PM", "02:02PM-04:00PM"]
# Output: 00:04


def turn_minutes(time):
    result = time[:-2].split(":")
    result = (
        [int(result[0]), int(result[1])]
        if time[-2:] == "AM"
        else [int(result[0]) + 12, int(result[1])]
    )
    result[0] = result[0] if (result[0] != 12 and result[0] != 24) else result[0] - 12
    return result[0] * 60 + result[1]


def MostFreeTime(strArr):
    times_list = []
    for time in strArr:
        times_list.append([turn_minutes(i) for i in time.split("-")])
    times_list.sort()
    most_free = 0
    for i in range(len(times_list) - 1):
        if times_list[i + 1][0] - times_list[i][1] > most_free:
            most_free = times_list[i + 1][0] - times_list[i][1]
    return "%02d:%02d" % (most_free / 60, most_free % 60)


# keep this function call here
# to see how to enter arguments in Python scroll down


input_str = ["10:00AM-12:30PM", "02:00PM-02:45PM", "09:10AM-09:50AM"]
print(MostFreeTime(input_str))




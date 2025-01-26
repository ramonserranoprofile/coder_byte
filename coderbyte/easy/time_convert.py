# Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the
# number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
# Separate the number of hours and minutes with a colon.

def TimeConvert(num):
    hours = num // 60
    minutes = num % 60
    return f"{hours}:{minutes}"

# keep this function call here
print(TimeConvert(int(input())))


# def TimeConvert(num):
#     return str(num / 60) + ":" + str(num % 60)

# Using the Python language, have the function Consecutive(arr) take the array of integers stored in arr and return the
# minimum number of integers needed to make the contents of arr consecutive from the lowest number to the highest
# number. For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the
#  array (5 and 7) to make it a consecutive array of numbers from 4 to 8. Negative numbers may be entered as parameters
# and no array will have less than 2 elements.


def Consecutive(an_array):
    an_array.sort()
    maximum = max(an_array)
    minimum = min(an_array)

    missing_nums = []
    for num in range(minimum, maximum):
        if num not in an_array:
            missing_nums.append(num)

    return len(missing_nums)

# keep this function call here
# to see how to enter arguments in Python scroll down
print(Consecutive(list(map(int, input("Input array: ").strip("[]").split(",")))))

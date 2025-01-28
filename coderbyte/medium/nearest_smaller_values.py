# Nearest Smaller Values
# The goal of this function is to find the nearest smaller value for each element in an array. For each element in the array, we look at the elements to its left and find the closest one that is smaller or equal to the current element. If no such element exists, we return -1 for that position.
# Example:
# Input: [3, 5, 2, 4, 5]
# Output: [-1, 3, -1, 2, 4]
# Explanation:
# For the first element, there is no smaller element to the left, so we return -1.
# For the second element, the closest smaller element is 3.
# For the third element, there is no smaller element to the left, so we return -1.
# For the fourth element, the closest smaller element is 2.
# For the fifth element, the closest smaller element is 4.


def NearestSmallerValues(arr):
    # code goes here
    output_arr = [-1]

    for num_id in range(1, len(arr)):

        appended_smaller = False

        for num in reversed(arr[:num_id]):
            if num <= arr[num_id]:
                output_arr.append(num)
                appended_smaller = True
                break

        if appended_smaller == False:
            output_arr.append(-1)

    return " ".join(str(num) for num in output_arr)


# keep this function call here
print(NearestSmallerValues([5, 2, 8, 3, 4]))  # [-1, -1, 2, 2, 3]


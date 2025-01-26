# Moving Median
# Have the function MovingMedian(arr) read the array of numbers stored in arr which will contain a sliding window size, N, as the first element in the array and the rest will be a list of numbers. Your program should return the Moving Median for each element based on the element and its N-1 predecessors, where N is the sliding window size. The final output should be a string with the moving median corresponding to each entry in the original array separated by commas.

# Note that for the first few elements (until the window size is reached), the median is computed on a smaller number of entries. For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] then the moving median output will be "1,2,3,5,6,6,4,3"

# Examples
# Input: [3, 1, 3, 5, 10, 6, 4, 3, 1]
# Output: 1,2,3,5,6,6,4,3

# Input: [5, 2, 4, 6]
# Output: 2,3,4


def MovingMedian(arr):
    N = arr[0]  # The size of the sliding window
    result = []

    for i in range(1, len(arr)):
        # Get the current window of elements
        if i < N:
            current_window = arr[1 : i + 1]  # Elements from index 1 to i
        else:
            current_window = arr[i - N + 1 : i + 1]  # Last N elements

        # Calculate the median
        sorted_window = sorted(current_window)
        mid_index = len(sorted_window) // 2

        if len(sorted_window) % 2 == 0:
            # If even number of elements, average the two middle numbers
            median = (sorted_window[mid_index - 1] + sorted_window[mid_index]) / 2
        else:
            # If odd number of elements, take the middle number
            median = sorted_window[mid_index]

        result.append(round(median))  # Round to nearest integer

    return ",".join(map(str, result))


# Test cases
print(MovingMedian([3, 1, 3, 5, 10, 6, 4, 3, 1]))  # Expected output: "1,2,3,5,6,6,4,3"
print(MovingMedian([5, 2, 4, 6]))  # Expected output: "2,3,4"

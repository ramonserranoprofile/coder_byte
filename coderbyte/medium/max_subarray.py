# max Subarray
# Medium
# Have the function MaxSubarray(arr) take the array of numbers stored in arr and determine the largest sum that can be formed by any contiguous subarray in the array. For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11 because the sum is formed by the subarray [5, -1, 7]. Adding any element before or after this subarray would make the sum smaller.

# Examples
# Input: [1, -2, 0, 3]
# Output: 3
# Input: [3, 4, -1, 1, -4]
# Output: 8

def MaxSubarray(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# keep this function call here
print(MaxSubarray(list(map(int, input().split(',')))))
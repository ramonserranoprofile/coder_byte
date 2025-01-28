# Parallel Sums
# Description:
# Have the function ParallelSums(arr) take the array of integers stored in arr and determine how they can be split into two even sets of integers each, such that both sets add up to the same number. If this is impossible return -1. If it's possible to split the array into two sets, then return a string representation of the first set followed by the second set with each element in the set being separated by a comma. E.g: if arr is [16, 22, 35, 8, 20, 1, 21, 11] then your program should output 16,8,1,21 and 22,35,20,11.
# Examples:
# Input: [1, 2, 3, 4]
# Output: 1,4 and 2,3
# Input: [1, 2, 3, 4, 5]
# Output: -1

import itertools

def ParallelSums(arr):
    # code goes here
    combinations = set(itertools.combinations(arr, len(arr) // 2))
    for a in combinations:
        a_sum = sum(a)
        b = arr[:]
        for i in a:
            b.remove(i)
        b_sum = sum(b)
        if a_sum == b_sum:
            result = compose(list(a), b)
            return result
    return -1

def compose(a, b):
    a.sort()
    b.sort()
    if a[0] <= b[0]:
        return ",".join(str(x) for x in a + b)
    else:
        return ",".join(str(x) for x in b + a)

# keep this function call here
print(ParallelSums([1, 2, 3, 4, 5]))

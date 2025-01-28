# Array Couples
# Description
# Have the function ArrayCouples(arr) take the arr parameter being passed which will be an array of an even number of positive integers, and determine if each pair of integers, [i, i+1], forms a couple such that for every pair, the element at i is an even number and the element at i+1 is an odd number. For example: if arr is [2, 6, 1, 7, 4, 2, 5, 2] then your program should output the string yes because each of the pairs is a couple. Another example: if arr is [2, 6, 1, 7, 4, 2, 6, 1] then your program should output the string no because the second pair is not a couple. Pairs should be unique and the elements at i and i+1 are in the correct order.
# Examples
# Input: [2, 6, 1, 7, 4, 2, 5, 2]
# Output: yes
# Input: [2, 6, 1, 7, 4, 2, 6, 1]
# Output: no
# Tags
# array
# Examples:    
# Input: [2, 6, 1, 7, 4, 2, 5, 2]
# Output: yes


def ArrayCouples(arr):
    pairs_with_id = []
    pairs = []
    all_pairs_with_id = []
    correct_pairs = []

    for element_id in range(0, len(arr) - 1, 2):
        pairs_with_id.append(([arr[element_id], arr[element_id + 1]], element_id))
        pairs.extend([arr[element_id], arr[element_id + 1]])
    for element_id in range(0, len(arr) - 1):
        all_pairs_with_id.append(([arr[element_id], arr[element_id + 1]], element_id))

    for pair in pairs_with_id:
        for pair_reversed in all_pairs_with_id:
            if pair[1] != pair_reversed[1]:
                if pair[0][::-1] == pair_reversed[0]:
                    correct_pairs.extend(pair[0])
                    break

    result = []

    for element in pairs:
        if element not in correct_pairs:
            result.append(element)

    if len(result) != 0:
        return ",".join(str(element) for element in result)

    return "yes"

# keep this function call here
input = [6, 2, 2, 6, 5, 1, 5]
print(ArrayCouples(input))

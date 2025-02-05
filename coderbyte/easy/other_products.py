# Other Products

# Have the function OtherProducts(arr) take the array of numbers stored in arr and return a new list of the products of all the other numbers in the array for each element.
# For example: if arr is [1, 2, 3, 4, 5] then the new array, where each location in the new array is the product of all other elements, is [120, 60, 40, 30, 24]. The following calculations were performed to get this answer: [(2*3*4*5), (1*3*4*5), (1*2*4*5), (1*2*3*5), (1*2*3*4)].
# You should generate this new array and then return the numbers as a string joined by a hyphen: 120-60-40-30-24. The array will contain at most 10 elements and at least 1 element and each element will be a number greater than or equal to 1.
# Examples
# Input: [1, 2, 3, 4, 5]
# Output: 120-60-40-30-24
# Input: [1, 4, 3]
# Output: 12-3-4



def OtherProducts(arr):
    # code goes here
    new_arr = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        new_arr.append(product)
    return new_arr

# keep this function call here is an array of integers

print(OtherProducts(list(map(int, input().split(','))))) # input() is a string, so we need to convert it to a list of integers
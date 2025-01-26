# Using the Python language, have the function ArrayAddition(arr) take the array of numbers stored in arr and return
# the string true if any combination of numbers in the array can be added up to equal the largest number in the array,
# otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true
# because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain
# negative numbers.
# Examples
# Input: [5, 7, 16, 1, 2]
# Output: false
# Input: [3, 5, -1, 8, 12]
# Output: true


def ArrayAddition(arr):
   
    max_num = max(arr)
    
    arr.remove(max_num)

    def can_sum_to_max(target, numbers):
        
        if target == 0:
            return True
        
        if target < 0 or not numbers:
            return False
        
        return can_sum_to_max(target - numbers[0], numbers[1:]) or can_sum_to_max(
            target, numbers[1:]
        )

    
    return can_sum_to_max(max_num, arr)


# Convierte la entrada del usuario a una lista de enteros
print(ArrayAddition(list(map(int, input("Input array: ").strip("[]").split(",")))))

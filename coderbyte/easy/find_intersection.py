# Find Intersection
# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
# Examples
# Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
# Output: 1,4,13
# Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
# Output: 1,9,10

def FindIntersection(strArr):

    list_1 = [int(x.strip()) for x in strArr[0].split(",")]
    list_2 = [int(x.strip()) for x in strArr[1].split(",")]

    sorted_intersect = sorted(list(set(list_1) & set(list_2)))

    return (
        ",".join([str(x) for x in sorted_intersect])
        if (len(sorted_intersect) > 0)
        else "false"
    )
    # code goes here


# keep this function call here
print(FindIntersection(input()))


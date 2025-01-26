# Min Window Substring
# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.
# Examples
# Input: ["ahffaksfajeeubsne", "jefaa"]
# Output: aksfaje
# Input: ["aaffhkksemckelloe", "fhea"]
# Output: affhkkse

def MinWindowSubstring(strArr):   
    N = strArr[0]
    K = strArr[1]
    char_count_K = {}
    for char in K:
        char_count_K[char] = char_count_K.get(char, 0) + 1
    char_count_window = {}
    left = 0
    min_lenght = float("inf")
    min_window = ""
    required = len(char_count_K)
    formed = 0
    for right in range(len(N)):
        char = N[right]
        char_count_window[char] = char_count_window.get(char, 0) + 1
        if char in char_count_K and char_count_window[char] == char_count_K[char]:
            formed += 1
            while left <= right and formed == required:
                window_length = right - left + 1
                if window_length < min_lenght:
                    min_lenght = window_length
                    min_window = N[left : right + 1]
                char_count_window[N[left]] -= 1
                if N[left] in char_count_K and char_count_window[N[left]] < char_count_K[N[left]]:
                    formed -= 1
                left += 1
    return min_window
# keep this function call here
print(MinWindowSubstring(input().split(",")))





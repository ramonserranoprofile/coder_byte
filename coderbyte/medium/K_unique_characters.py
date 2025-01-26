# K Unique Characters
# Medium
# Have the function KUniqueCharacters(str) take the str parameter being passed and find the longest substring that contains
# k unique characters, where k will be the first character from the string. The substring will start from the second position
# in the string because the first character will always be a unique character. For example: if str is "2aabbacbaa" there are
# several substrings that all contain 2 unique characters, namely: ["aabba", "ac", "cb", "ba"], but your program should return
# "aabba" because it is the longest substring. If there are multiple longest substrings, then return the first one that
# appeared.


def KUniqueCharacters(strParam):
    k = int(strParam[0])
    strParam = strParam[1:]
    longest = ""
    for i in range(len(strParam)):
        for j in range(i + 1, len(strParam) + 1):
            substring = strParam[i:j]
            if len(set(substring)) == k:
                if len(substring) > len(longest):
                    longest = substring
    return longest


print(KUniqueCharacters("2aabbacbaa"))  # aabba
print(KUniqueCharacters("3aabacbebebe"))  # cbebebe
print(KUniqueCharacters("1a"))  # a 
print(KUniqueCharacters("3abcabcabc"))  # abcabcabc
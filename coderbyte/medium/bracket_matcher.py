# Bracket Matcher
# Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
# Examples
# Input: "(coder)(byte))"
# Output: 0
# Input: "(c(oder)) b(yte)"
# Output: 1

def BracketMatcher(strParam):
    open_brackets = 0
    for char in strParam:
        if char == "(":
            open_brackets += 1
        if char == ")":
            open_brackets -= 1
        if open_brackets < 0:
            return 0
    return 0 if open_brackets != 0 else 1

# keep this function call here
print(BracketMatcher(input()))

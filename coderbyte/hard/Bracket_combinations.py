# Bracket Combinations
# Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, and return the number of valid combinations that can be formed with num pairs of parentheses. For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). There are 5 total combinations when the input is 3, so your program should return 5.
# Examples
# Input: 3
# Output: 5
# Input: 2
# Output: 2

def BracketCombinations(num):
  if num == 0:
    return 1
 
  # code goes here
  from math import factorial
  return factorial(2*num) // (factorial(num+1)*factorial(num))

# keep this function call here 
print(BracketCombinations(int(input())))
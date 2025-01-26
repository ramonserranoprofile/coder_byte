# GCF: Greatest Common Factor
# GCF: Greatest Common Factor
# Have the function GCF(num1,num2) take both parameters being passed and return the Greatest Common Factor.
# The Greatest Common Factor between two numbers is the largest number that both numbers can divide into.
# For example: 12 and 16 both can be divided by 1, 2, and 4 so the output should be 4.
# Examples
# Input: 7 & 3
# Output: 1
# Input: 36 & 54
# Output: 18
# Tags
# math fundamentals

def GCF(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# keep this function call here
# to see how to enter arguments in Python scroll down
print(GCF(int(input()), int(input())))


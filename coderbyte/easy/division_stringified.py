# Division Stringified
# Have the function DivisionStringified(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas. If an answer is only 3 digits long, return the number with no commas (ie. 2 / 3 should output "1"). For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346".

# Examples
# Input: 5 & num2 = 2
# Output: "3"
# Input: 6874 & num2 = 67
# Output: "103"
# Tags
# string manipulation, math fundamentals

def DivisionStringified(num1,num2): 
    return "{:,}".format(int(round(float(num1)/num2)))
    
# keep this function call here

print(DivisionStringified(123456789, 10000)) # "12,346"
print(DivisionStringified(5, 2)) # "3"
print(DivisionStringified(6874, 67)) # "103"
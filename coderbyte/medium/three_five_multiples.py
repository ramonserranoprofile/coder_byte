# Three Five Multiples
# Examples:
# Imput 17
# Output 60

def ThreeFiveMultiples(num):
    return sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0)


# keep this function call here
# to see how to enter arguments in Python scroll down

print(ThreeFiveMultiples(int(input())))  # 17 output 60


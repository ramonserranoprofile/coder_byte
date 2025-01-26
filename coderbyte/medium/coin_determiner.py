# Coin Determiner
# Examples:
# Input 16
# Output 2

# Have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, and return an integer output that will specify the least number of coins, that when added together, equal the input integer. Coins are based on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11. So for example: if num is 16, then the output should be 2 because you can achieve the 16 by adding two 9s together. If num is 25, then the output should be 3 because you can achieve 25 by adding two 7s and a 9.

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def CoinDeterminer(num):
    coins = [11, 9, 7, 5, 1]
    count = 0
    for coin in coins:
        while num >= coin:
            num -= coin
            count += 1
    return count


# keep this function call here
print(CoinDeterminer(int(input())))


# Have the function PrimeChecker(num) take num and return 1 if any arrangement of num comes out to be a prime number,
# otherwise return 0. For example: if num is 910, the output should be 1 because 910 can be arranged into 109 or 019,
# both of which are primes.

import itertools
import math


def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for potential_factor in range(2, int(math.sqrt(num) + 1)):
        if num % potential_factor == 0:
            return False
    return True

def PrimeChecker(num):
    perms = [int(''.join(perm)) for perm in itertools.permutations(str(num))]

    list_perms = list(set(perms))
    list_perms.sort()

    for potential_prime in list_perms:
        if is_prime(potential_prime):
            return 1
    return 0

# keep this function call here
# to see how to enter arguments in Python scroll down
print(PrimeChecker(int(input("Input num: "))))

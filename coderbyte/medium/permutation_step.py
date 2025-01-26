#  Using the Python language, have the function PermutationStep(num) take the num parameter being passed and return the
# next number greater than num using the same digits. For example: if num is 123 return 132, if it's 12453 return 12534.
#  If a number has no greater permutations, return -1 (ie. 999).


def get_permutations(num):
    # Function to generate all permutations of a number
    num_str = str(num)
    permutations = set()

    def permute(s, start=0):
        if start == len(s) - 1:
            permutations.add(int("".join(s)))
        else:
            for i in range(start, len(s)):
                s[start], s[i] = s[i], s[start]  # Swap
                permute(s, start + 1)  # Recurse
                s[start], s[i] = s[i], s[start]  # Swap back

    permute(list(num_str))  # Call the helper function
    return sorted(permutations)


def PermutationStep(num):
    perms = get_permutations(num)
    num_index = perms.index(num)

    try:
        if perms[num_index + 1] > num:
            return perms[num_index + 1]
        return -1
    except IndexError:
        return -1

# keep this function call here
# to see how to enter arguments in Python scroll down
print(PermutationStep(int(input("Input num: "))))

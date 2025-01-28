# Line Ordering
# Description:
#     Have the function LineOrdering(strArr) read the strArr parameter being passed which will be a list of strings
#     which models a bunch of relationships between people standing in a line. Each string will contain a
#     source person and a destination person, which will form a relationship of independent or dependent states.

#     These relationships will be represented by an underscore, which means that these two persons are in
#     whatever state they are in, but the relative order of the string will be maintained. Your goal is to
#     determine a correct order for the strings such that a dependent relationship is implied through the order.

#     For example: if strArr is ["A>B","B>C","C> D"], then A is an independent person, B is dependent on A,
#     C is dependent on B, and D is dependent on C. So A should be placed before B, B before C, and C before D.
#     So your program should return the string abcd.

#     Another example: if strArr is ["J>B","B>S","S>K"], then J is dependent on B, B is dependent on S, and K is
#     dependent on S, so J should be placed before B and B before S, so that the final string will be bjks.
# Input: ["A>B","A>C","B>D","D>C"]
# Output: acdb
# Input: ["A>B","A>C","C>B","D>A"]
# Output: acbd
# Input: ["J>B","B>S","S>K","K>J"]
# Output: bjks

from itertools import permutations

def LineOrdering(strArr):
    # code goes here
    people = set()
    output = []
    for condition in strArr:
        condition = condition.replace("&#60;", "<")
        people.add(condition[0])
        people.add(condition[2])

    permutation = list(permutations(people))

    for path in permutation:
        add = True
        for condition in strArr:
            if condition[1] == ">":
                if path.index(condition[0]) < path.index(condition[-1]):
                    add = False
            else:
                if path.index(condition[0]) > path.index(condition[-1]):
                    add = False

        if add:
            output.append(path)

    return (output)
    # return len(output)

# keep this function call here
print(LineOrdering(["J>B", "B>S", "S>K", "K>J"])) # 0
print(LineOrdering(["A>B", "A>C", "B>D", "D>C"])) # 1
print(LineOrdering(["A>B", "A>C", "C>B", "D>A"])) # 1
print(LineOrdering(["J>B", "B>S", "S>K", "K>J"]))  # 1

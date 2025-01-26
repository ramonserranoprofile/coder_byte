# Tree Constructor
# Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:

# which you can see forms a proper binary tree. Your program should, in this case, return the string true because a valid binary tree can be formed. If a proper binary tree cannot be formed with the integer pairs, then return the string false. All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.
# Examples
# Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# Output: true
# Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
# Output: false



def TreeConstructor(strArr):
    pairs = [pair.strip("()").split(",") for pair in strArr]
    tree = {}
    for child, parent in pairs:
        if child not in tree:
            tree[child] = {"parent": None, "children": []}
        if parent not in tree:
            tree[parent] = {"parent": None, "children": []}
        tree[child]["parent"] = parent
        tree[parent]["children"].append(child)
        has_at_most_two_children = all(
            len(node["children"]) <= 2 for node in tree.values()
        )
        single_root = (
            len([node for node in tree.values() if node["parent"] is None]) == 1
        )
    # code goes here
    return has_at_most_two_children and single_root

# keep this function call here
print(TreeConstructor(input()))

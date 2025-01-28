# Step Walking
# Description:
# Have the function StepWalking(num) take the num parameter being passed which will be an integer between 1 and 1,000 that represents the number of steps already taken. You can assume the person always starts at step 1. That means num will be a positive integer from 1 to 1,000. Use the parameter being passed to determine the number of ways to walk 2 steps, and return the number of different ways how the person can walk 2 steps exactly. For example, if num is 3, then your program should return 4 because there are four ways to walk the steps. (1 step + 1 step, 1 step + 2 steps, 2 steps + 1 step, 2 steps + 2 steps).
# Sample Test Cases:
# Input: 3
# Output: 4

# Input: 4
# Output: 7

def StepWalking(num):
    # code goes here
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return StepWalking(num - 1) + StepWalking(num - 2)


# keep this function call here
print(StepWalking(int(input())))

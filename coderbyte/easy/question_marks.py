# Questions Marks
# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
# Examples
# Input: "aa6?9"
# Output: false
# Input: "acc?7??sss?3rr1??????5"
# Output: true



def QuestionsMarks(strParam):  
    last_number = None

    question_count = 0

    valid_pair_found = False

    for char in strParam:
        if char.isdigit():
            current_number = int(char)
            if last_number is not None and last_number + current_number == 10:

                if question_count == 3:
                    valid_pair_found = True
                else:
                    return "false"

            last_number = current_number
            question_count = 0
        elif char == "?":
            question_count += 1

    return "true" if valid_pair_found else "false"

# keep this function call here
print(QuestionsMarks(input()))

# Multiple Brackets

def MultipleBrackets(strParam):
    count = 0
    countList = []
    for i in strParam:
        if i == "(" or i == "[":
            count += 1
            countList.append(i)
        elif i == ")" or i == "]":
            if countList.pop() != ("(" if i == ")" else "["):
                return 0
    return "%d %d" % (1, count) if len(countList) == 0 else 0


# keep this function call here
# to see how to enter arguments in Python scroll down
print(MultipleBrackets(str(input())))


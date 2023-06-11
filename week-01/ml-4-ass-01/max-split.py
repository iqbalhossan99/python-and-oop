
# s = input()

# def MaxSplit(s):
#     n = len(s)
#     splitResult = []
#     count = 0
#     tempString = ""

#     for i in range(n):
#         tempString += s[i]
#         if s[i] == 'L':
#             count += 1
#         else:
#             count -= 1

#         if count == 0:
#             splitResult.append(tempString)
#             tempString = ""

#     return len(splitResult), splitResult

# num_strings, balanced_strings = MaxSplit(s)

# print(num_strings)


# for string in balanced_strings:
#     print(string)


"""
new code 
"""

s = input()
def MaxSplit(s):
    n = len(s)
    splitResult = []
    count = 0
    tempString = ""

    for i in range(n):
        tempString += s[i]

        if s[i] == 'L':
            count += 1
        else:
            count -= 1

        if count == 0:
            splitResult.append(tempString)
            tempString = ""

    return splitResult


balancedStrings = MaxSplit(s)
balancedStringNumber = len(balancedStrings)
print(balancedStringNumber)

for st in balancedStrings:
    print(st)
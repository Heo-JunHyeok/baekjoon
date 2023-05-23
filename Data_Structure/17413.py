# import sys

# stack = ""
# result = ""
# check = False # < > 태그 여부

# for s in sys.stdin.readline().rstrip():
#     if s == "<":
#         check = True
#         result = result + stack[::-1] + s
#         stack = ""
#         continue
#     elif s == ">":
#         check = False
#         result += s
#         continue
#     elif s == " ":
#         if check:
#             result += " "
#         else:
#             result = result + stack[::-1] + " "
#             stack = ""
#         continue

#     if check:
#         result += s
#     else:
#         stack += s

# print(result + stack[::-1])


import sys
from collections import deque

stack = deque()
result = ""
check = False  # < > 태그 여부

for s in sys.stdin.readline().rstrip():
    if s == "<":
        while stack:
            result += stack.pop()
        result += s
        check = True
        continue
    elif s == ">":
        check = False
        result += s
        continue
    elif s == " ":
        if check:
            result += " "
        else:
            while stack:
                result += stack.pop()
            result += " "
        continue

    if check:
        result += s
    else:
        stack.append(s)

print(result + "".join(stack)[::-1])

import sys


notation = sys.stdin.readline().rstrip()
stack = []
result = ""

for i in notation:
    if i.isupper():
        result += i
    else:
        if i == "(":
            stack.append(i)
        elif i == "*" or i == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()

print(result + "".join(stack)[::-1])

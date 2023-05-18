import sys

# 커서를 기준으로 왼쪽 string, 오른쪽 stack
string = list(sys.stdin.readline().strip())
stack = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    if command[0] == "L":
        if string:
            stack.append(string[-1])
            string.pop()
    elif command[0] == "D":
        if stack:
            string.append(stack[-1])
            stack.pop()
    elif command[0] == "B":
        if string:
            string.pop()
    else:
        string.append(command[1])

# stack = list(reversed(stack))
stack = stack[::-1]

print("".join(string + stack))

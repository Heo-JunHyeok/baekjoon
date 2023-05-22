import sys
from collections import deque

n = int(sys.stdin.readline())
result = deque()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        result.appendleft(command[1])
    elif command[0] == "push_back":
        result.append(command[1])
    elif command[0] == "pop_front":
        if result:
            print(result.popleft())
        else:
            print("-1")
    elif command[0] == "pop_back":
        if result:
            print(result.pop())
        else:
            print("-1")
    elif command[0] == "empty":
        if result:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if result:
            print(result[0])
        else:
            print("-1")
    elif command[0] == "back":
        if result:
            print(result[-1])
        else:
            print("-1")
    else:
        print(len(result))

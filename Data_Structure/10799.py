import sys
from collections import deque

stack = deque()
bar = 0
razer = True

for s in sys.stdin.readline().rstrip():
    if s == "(":
        stack.append(s)
        razer = True
    else:
        stack.pop()
        if razer:
            bar += len(stack)
            razer = False
        else:
            bar += 1

print(bar)

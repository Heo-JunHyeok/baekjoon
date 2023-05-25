import sys
from collections import deque

a = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

result = [-1] * a
stack = deque()


for i in range(a):
    while stack and (array[stack[-1]] < array[i]):
        result[stack.pop()] = array[i]
    stack.append(i)

print(*result)

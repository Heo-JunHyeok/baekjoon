import sys
from collections import deque, Counter

n = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

count_array = Counter(array)
stack = deque()
result = [-1] * n

for i in range(n):
    while stack and (count_array[array[stack[-1]]] < count_array[array[i]]):
        result[stack.pop()] = array[i]
    stack.append(i)

print(*result)

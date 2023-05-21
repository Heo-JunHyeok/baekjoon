import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
result = []

for i in range(1, n + 1):
    queue.append(i)

for _ in range(n):
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("".join(str(result)).replace("[", "<").replace("]", ">"))

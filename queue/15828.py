import sys
from collections import deque

queue = deque()
n = int(input())

while (x := int(sys.stdin.readline())) != -1:
    if x == 0:
        queue.popleft()
    elif len(queue) < n:
        queue.append(x)


if queue:
    print(" ".join(map(str, list(queue))))
else:
    print("empty")

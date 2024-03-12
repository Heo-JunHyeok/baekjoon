from collections import deque

n = int(input())
card = [i for i in range(1, n + 1)]
queue = deque()

queue.extend(card)

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])

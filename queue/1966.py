from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0

    while queue:
        if queue[0] == max(queue):
            q = queue.popleft()
            cnt += 1
            if m == 0:
                print(cnt)
                break
        else:
            queue.rotate(-1)
            
        if m == 0:
            m = len(queue) - 1
        else:
            m -= 1

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
result = []

# queue에 1~n까지 저장
for i in range(1, n + 1):
    queue.append(i)


for _ in range(n):
    # k-1 번째까지 수를 queue의 마지막으로 이동
    for _ in range(k - 1):
        queue.append(queue.popleft())

    # k 번째 수를 queue에서 삭제 및 결과값에 추가
    result.append(queue.popleft())

print("".join(str(result)).replace("[", "<").replace("]", ">"))

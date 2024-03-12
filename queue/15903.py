import sys
import heapq as hq


n, m = map(int, sys.stdin.readline().strip().split())

pq = list(map(int, sys.stdin.readline().strip().split()))
hq.heapify(pq)

for i in range(m):
    root = hq.heappop(pq)
    root += hq.heappop(pq)

    hq.heappush(pq, root)
    hq.heappush(pq, root)

print(sum(pq))

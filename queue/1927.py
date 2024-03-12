import sys
import heapq as hq

pq=[]

for _ in range(int(sys.stdin.readline())):
    x=int(sys.stdin.readline())
    if x!=0:
        hq.heappush(pq, x)
    else:
        if len(pq)!=0:
            print(hq.heappop(pq))
        else:
            print('0')
    
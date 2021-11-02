import sys

n=int(sys.stdin.readline())
a=[0]*10001

for i in range(n):
    a[int(sys.stdin.readline().strip())]+=1

for i in range(1,10001):
    for _ in range(a[i]):
        print(i)

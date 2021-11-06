import sys

n=int(sys.stdin.readline())
a=[]
for _ in range(n):
    a.append(sys.stdin.readline().split())

a.sort(reverse=0)

for i in a:
    print(' '.join(i))
import sys

n=int(sys.stdin.readline())
a=[]

for _ in range(n):
    a.append(sys.stdin.readline().strip())

a=list(set(a))

a.sort(key=lambda x:(len(x),x))

print('\n'.join(a))
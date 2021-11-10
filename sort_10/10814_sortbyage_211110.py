import sys

n=int(sys.stdin.readline())
a=[]

for _ in range(n):
    age,name=sys.stdin.readline().split()
    a.append([int(age),name])

a.sort(key=lambda x:x[0])

for x,y in a:
    print(x,y)

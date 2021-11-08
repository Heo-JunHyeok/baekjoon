import sys

n=int(sys.stdin.readline())
a=[]

for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))

a.sort(key=lambda a : (a[1], a[0]))
                
for x,y in a:
    print(x,y)
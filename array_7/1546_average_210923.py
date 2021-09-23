import sys

n = int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
new_a=[]

m=max(a)

for i in a:
    new_a.append(i/m*100)

av=sum(new_a)/n

print(av)
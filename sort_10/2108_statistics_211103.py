import sys

n=int(sys.stdin.readline())
a=[]
c=[0]*4
temp=0

for _ in range(n):
    a.append(int(sys.stdin.readline().strip()))

a.sort(reverse=0)
b=list(set(a))
b.sort(reverse=0)
for i in range(len(b)):
    if temp<a.count(b[i]):
        temp=a.count(b[i])
        c[2]=b[i]

c[0]=round(sum(a)/n)
c[1]=a[(n//2)+1]
c[3]=max(a)-min(a)

for i in c:
    print(i)
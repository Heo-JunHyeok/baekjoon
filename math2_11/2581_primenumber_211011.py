import sys

m=int(sys.stdin.readline())
n=int(sys.stdin.readline())
total=0
a=[]

for i in range(m,n+1):
    primecheck=True
    for j in range(2,(i//2)+1):
        if i%j==0:
            primecheck=False
            break
    if primecheck==True and i!=1:
        total+=i
        a.append(i)

if total==0: print(-1)
else: 
    print(total)
    print(min(a))

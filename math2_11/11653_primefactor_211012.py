import sys

n=int(sys.stdin.readline())
a=[]

def factor(n):
    n=int(n)
    for i in range(2,n+1):
        if n%i==0:
            a.append(i)
            return factor(n//i)

if n!=1:
    factor(n)
    for i in a:
        print(i)

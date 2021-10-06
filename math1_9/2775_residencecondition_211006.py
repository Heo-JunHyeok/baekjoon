import sys

t=int(sys.stdin.readline())

for i in range(t):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    nume,demo=1,1

    for i in range(n,n+k+1):
        nume*=i

    for i in range(1,k+2):
        demo*=i

    result=nume//demo

    print(result)
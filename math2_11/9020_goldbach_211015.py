import sys

t=int(sys.stdin.readline())
a=[True]*(10001)

for i in range(2,int(10000**0.5)+1):
    if a[i]:
        for j in range(i+i,10001,i):
            a[j]=False

for i in range(t):
    n=int(sys.stdin.readline())
    diff=10000

    for j in range(2,n//2+1):
        if a[j]==True and a[n-j]==True:
            if j==(n-j):
                x,y=j,n-j
                break
            elif abs(n-2*j)<diff:
                diff=abs(n-2*j)
                x,y=j,n-j
    sys.stdout.write(str(x)+' '+str(y)+'\n')

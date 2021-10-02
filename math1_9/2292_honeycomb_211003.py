import sys

n=int(sys.stdin.readline())
a=[1]

if n==1:
    print(1)
else:
    i=0
    while True:
        a.append(a[i]+6*(i+1))
        if n<=a[i+1]:
            print(i+2)
            break
        i+=1
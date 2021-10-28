import sys

n=int(sys.stdin.readline())

for a in range(1,n):
    sum=0
    for i in str(a):
        sum+=int(i)
    if (a+sum)==n:
        print(a)
        break
    a+=1
else:
    print('0')
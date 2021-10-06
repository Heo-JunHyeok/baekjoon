import sys

n=int(sys.stdin.readline())
i=n//5

while i>=0:
    temp=n-5*i
    if temp%3==0:
        print(i+temp//3)
        break
    i-=1
else:
    print(-1)
import sys

n=int(sys.stdin.readline())

a=list(map(int,sys.stdin.readline().split()))
result=0

if 1 in a:
    a.remove(1)

for i in a:
    cnt=0
    for j in range(2,i):
        if i%j==0:
            cnt+=1
        if cnt==1:
            break
    if cnt==0:
        result+=1

print(result)

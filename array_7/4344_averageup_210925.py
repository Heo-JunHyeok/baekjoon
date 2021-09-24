import sys

c=int(sys.stdin.readline())
cnt=0

for i in range(c):
    n=list(map(int,sys.stdin.readline().split()))
    s=sum(n[1:])/n[0]
    for j in n[1:]:
        if j>s:
            cnt+=1
    rate=cnt/n[0]*100
    print('{:.3f}%'.format(round(rate,3)))
    cnt=0

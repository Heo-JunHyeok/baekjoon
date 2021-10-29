import sys

n=int(sys.stdin.readline())
a=[]

for i in range(n):
    a.append(sys.stdin.readline().split())

for i in a:
    cnt=1
    for k in a:
        if int(i[0])<int(k[0]) and int(i[1])<int(k[1]):
            cnt+=1
    print(cnt,end=' ')

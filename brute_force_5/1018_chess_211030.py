import sys

n,m=map(int,sys.stdin.readline().split())
a=[]

for i in range(n):
    a.append(sys.stdin.readline().strip())

for i in a:
    for j in i[:-7]:
        for k in i[a.index(j)+1:a.index(j)+8]:
            print(k)
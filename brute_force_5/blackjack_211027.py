import sys

n,m=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
result=0

for i in a[:-2]:
    for j in a[a.index(i)+1:-1]:
        if (i+j)<m:
            for k in a[a.index(j)+1:]:
                if result<(i+j+k)<=m:
                    result=i+j+k

print(result)
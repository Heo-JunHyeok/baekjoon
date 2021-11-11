import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

b=sorted(list(set(a)))

c=dict()
for i in range(len(b)):
    c[b[i]]=i
# c={k:v for v,k in enumerate(b)}

for i in a:
    if i in c.keys():
        sys.stdout.write(str(c[i])+' ')
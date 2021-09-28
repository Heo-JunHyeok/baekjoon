import sys

word=sys.stdin.readline().strip().upper()
a=dict()
cnt=0
result=[]

for i in word:
    if i in a:
        a[i]+=1
    else:
        a[i]=1

b=max(a.values())
for i in a:
    if a[i]==b:
        cnt+=1
        result.append(i)

if cnt>1:
    print('?')
else:
    for i in result:
        print(i)
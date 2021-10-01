import sys

n=int(sys.stdin.readline())
a=[]
temp=[]

for i in range(n):
    a.append(list(sys.stdin.readline().strip()))

for i in a:
    temp.append(i[0])
    if len(i)>1:
        for j in i[1:]:
            if j in temp and temp[-1]!=j:
                n-=1
                break
            elif j not in temp:
                temp.append(j)
    temp.clear()

print(n)
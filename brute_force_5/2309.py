import sys

a=[]

for _ in range(9):
    a.append(int(sys.stdin.readline().strip()))
    
a.sort()
remain=sum(a)-100

for i in range(0,9):
    for j in a[i+1:]:
        if a[i]+j == remain:
            remain=[a[i],j]
            break
            
result = [i for i in a if i not in remain]
print("\n".join(map(str,result)))
    
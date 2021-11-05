import sys

n=str(sys.stdin.readline().strip())
m=[]

for i in n:
    m.append(i)

m.sort(reverse=1)
    
for i in m:
    print(i,end='')
#print(''.join(a))
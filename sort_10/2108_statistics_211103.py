import sys

n=int(input())
a=[int(sys.stdin.readline().strip()) for _ in range(n)]
  
a.sort()

print(round(sum(a)/n)) 
print(a[n//2]) 

fre= [0]*8001 
   
for i in a:
    fre[i+4000]+=1 
    
if fre.count(max(fre))==1: 
    print(fre.index(max(fre))-4000)
    
else:   
  
    m=0
    i=-1
    while m!=2:
        i+=1
        if fre[i]==max(fre):
            m+=1
        
    print(i-4000)
                
print(max(a)-min(a))

# 시간 초과
# import sys

# n=int(sys.stdin.readline())
# a=[]
# c=[]
# result=[0]*4

# for _ in range(n):
#     a.append(int(sys.stdin.readline().strip()))

# b=list(set(a))
# b.sort(reverse=0)

# for i in range(len(b)):
#     c.append(a.count(b[i]))

# if c.count(max(c))==1:
#     result[2]=b[c.index(max(c))]
# else:
#     cnt=0
#     for i in range(len(b)):
#         if c[i]==max(c):
#             cnt+=1
#         if cnt==2:
#             result[2]=b[i]
#             break

# a.sort(reverse=0)
# result[0]=round(sum(a)/n)
# result[1]=a[n//2]
# result[3]=max(a)-min(a)

# for i in result:
#     print(i)
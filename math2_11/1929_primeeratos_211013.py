import sys

m,n=map(int,sys.stdin.readline().split())
a=[True]*(n+1)

for i in range(2,int(n**0.5)+1):
    if a[i]:
        for j in range(i+i,n+1,i):
            a[j]=False

for i in range(m,n+1):
    if a[i]==True and i!=1:
        print(i)

# 시간초과
# a=[]

# for i in range(2,n+1):
#     primecheck=True
#     for j in range(i,n+1,i):
#         if primecheck:
#             primecheck=False
#             pass
#         else:
#             a.append(j)

# a=list(set(a))

# for i in range(m,n+1):
#     if i not in a and i!=1:
#         print(i)
        
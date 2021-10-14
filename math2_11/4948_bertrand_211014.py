import sys

a=[True]*(246913)

for i in range(2,int(246912**0.5)+1):
    if a[i]:
        for j in range(i+i,246913,i):
            a[j]=False

while True:
    n=int(sys.stdin.readline())
    if n==0: break
    elif n==1: sys.stdout.write(str(1))
    else:
        cnt=0
        for i in a[n+1:2*n]:
            if i == True:
                cnt+=1
        sys.stdout.write(str(cnt)+'\n')

# 시간 초과
# def prime(n):
#     n=int(n)
#     check=True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             check=False
#             return 0
#     if check:
#         return 1
    
# while True:
#     n=int(sys.stdin.readline())
#     if n==0: break
#     elif n==1: print(1)
#     else:
#         result=0
#         for i in range(n+1,2*n+1):
#             cnt=prime(i)
#             result+=cnt
#         sys.stdout.write(str(result)+'\n')
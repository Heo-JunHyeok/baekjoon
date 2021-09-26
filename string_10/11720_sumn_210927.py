import sys

n=int(sys.stdin.readline())
#   1  # 
# a=list(map(str,sys.stdin.readline().strip()))
# b=0
# for i in a:
#     b+=int(i)
# print(b)
a=list(sys.stdin.readline().strip())
print(sum(map(int,a)))
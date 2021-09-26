import sys

n=int(sys.stdin.readline())
a=list(sys.stdin.readline().strip())
# a=list(map(str,sys.stdin.readline().strip()))
# b=0
# for i in a:
#     b+=int(i)
print(sum(map(int,a)))
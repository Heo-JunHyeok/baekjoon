import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())

result=str(a*b*c)

for i in range(10):
    count=result.count(str(i))
    print(count)
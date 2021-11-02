import sys

n=int(sys.stdin.readline())
a=[]

for i in range(n):
    a.append(int(sys.stdin.readline().strip()))

a.sort()

for i in a:
    print(i)

#timsort = 삽입정렬+병합정렬
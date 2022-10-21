import sys


n, m = map(int, sys.stdin.readline().split())

l = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(sum(l[start - 1 : end]))

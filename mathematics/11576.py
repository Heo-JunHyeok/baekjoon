import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
ab_list = list(map(int, sys.stdin.readline().split()))
ten = 0

# A진법 -> 10진법
for i in range(m):
    ten += ab_list.pop() * (a**i)

# 10진법 -> B진법
while ten:
    ab_list.append(ten % b)
    ten //= b

print(*ab_list[::-1])

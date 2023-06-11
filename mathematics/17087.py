import sys


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

distance = []
for i in a:
    x = abs(s - i)
    if x != 0:
        distance.append(x)

result = distance[0]
for i in distance[1:]:
    result = gcd(i, result)

print(result)

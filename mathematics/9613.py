import sys
from itertools import combinations


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


for _ in range(int(sys.stdin.readline())):
    n = list(map(int, sys.stdin.readline().split()))

    com = list(combinations(n[1:], 2))

    g = 0
    for i in range(len(com)):
        g += gcd(com[i][0], com[i][1])

    print(g)

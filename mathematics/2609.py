import sys


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


a, b = map(int, sys.stdin.readline().split())
g = gcd(max(a, b), min(a, b))
l = a * b // g

print(g, l, sep="\n")

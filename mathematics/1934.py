import sys
import math

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    g = math.gcd(a, b)
    print(a * b // g)


# for _ in range(int(sys.stdin.readline())):
#     a, b = map(int, sys.stdin.readline().split())
#     print(math.lcm(a, b))

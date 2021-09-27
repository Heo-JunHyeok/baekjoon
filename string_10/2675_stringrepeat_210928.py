import sys

T=int(sys.stdin.readline())

for i in range(T):
    R,S=sys.stdin.readline().strip().split()
    for j in S:
        print(j*int(R),end='')
    print()
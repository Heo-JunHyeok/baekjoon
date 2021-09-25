import sys

def solve(a):
    ans=0
    for i in a:
        ans+=i
    return ans
# def solve(lst):
#     return sum(lst)
n=list(map(int,sys.stdin.readline().split()))

print(solve(n))
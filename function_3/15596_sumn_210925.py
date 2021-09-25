import sys

def solve(a):
    ans=0
    for i in range(a):
        ans+=i
    return ans
# def solve(lst):
#     return sum(lst)
#n=list(map(int,sys.stdin.readline().split()))
n=11
print(solve(n))
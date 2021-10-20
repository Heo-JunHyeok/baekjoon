import sys

def fibonacci(a,b,n):
    if n==0: print(a)
    else:
        return fibonacci(b,a+b,n-1)

n=int(sys.stdin.readline())

fibonacci(0,1,n)
import sys

def factorial(n,result):
    if n==0:
        print('1')
    else:
        result*=n
        if n>1:
            return factorial(n-1,result)
        elif n==1:
            print(result)

n=int(sys.stdin.readline())
result=1

factorial(n,result)
import sys

n=int(sys.stdin.readline())
chess=[[0]*n for i in range(n)]
count,result=0,0

def queen(count,result):
    if count == n:
        result += 1
        return
    
    for i in range(n)
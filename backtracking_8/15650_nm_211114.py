import sys

n, m = map(int,sys.stdin.readline().split())
a = []

def nm():
    if len(a) == m:
        print(' '.join(map(str, a)))
        return
    
    for i in range(1, n+1):
        if len(a)>=1:
            if i in a or i < a[-1]:
                continue
        a.append(i)
        nm()
        a.pop()
        
nm()
import sys

def small(a,b):
    a=int(a)
    b=int(b)
    if a<=b:
        return a
    else:
        return b

x,y,w,h=map(int,sys.stdin.readline().split())

horizontal=small(x,w-x)
vertical=small(y,h-y)
result=small(horizontal,vertical)

sys.stdout.write(str(result)+'\n')

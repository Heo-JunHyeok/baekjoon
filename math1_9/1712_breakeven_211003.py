import sys
import math

a,b,c=map(int,sys.stdin.readline().split())

if b<c:
    if a%(c-b) == 0:
        bep=(a//(c-b))+1
    else:
        bep=math.ceil(a/(c-b))
else:
    bep=-1

print(bep)

    
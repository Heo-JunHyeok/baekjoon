import sys

a,b,c=map(int,sys.stdin.readline().split())

while a!=0 and b!=0 and c!=0:
    m=max(a,b,c)
    if a**2+b**2+c**2==2*(m**2):
        sys.stdout.write('right'+'\n')
    else:
        sys.stdout.write('wrong'+'\n')
    
    a,b,c=map(int,sys.stdin.readline().split())
    
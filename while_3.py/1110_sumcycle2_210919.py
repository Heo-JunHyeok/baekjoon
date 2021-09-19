import sys

n = int(sys.stdin.readline())
first_n=n
cycle=0

while True:
    a=n//10
    b=n%10
    sumab=a+b
    n=b*10+sumab%10
    cycle+=1
    
    if n==first_n:
        break

print(f'{cycle}')

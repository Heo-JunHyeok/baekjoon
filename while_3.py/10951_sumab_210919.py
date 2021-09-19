import sys

while True:
    try:
        a,b = map(int,sys.stdin.readline().split())
        print(f'{a+b}')
    except:
        break
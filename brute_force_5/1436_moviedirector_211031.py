import sys

n=int(sys.stdin.readline())
cnt,a=0,666

while True:
    if '666' in str(a): cnt+=1
    if cnt==n:
        print(a)
        break
    a+=1

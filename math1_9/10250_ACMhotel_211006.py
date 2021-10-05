import sys

t=int(sys.stdin.readline())

for i in range(t):
    h,w,n=map(int,sys.stdin.readline().split())
    floor=n%h
    if n%h == 0:
        r_num=n//h
    else:
        r_num=n//h+1
    if r_num<10:
        print(str(floor)+str(r_num).zfill(2))
    else:
        print(str(floor)+str(r_num))
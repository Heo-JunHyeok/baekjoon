import sys

t=int(sys.stdin.readline())

for i in range(t):
    x_1,y_1,r_1,x_2,y_2,r_2=map(int,sys.stdin.readline().split())

    d=(x_2-x_1)**2+(y_2-y_1)**2    
    if x_1==x_2 and y_1==y_2 and r_1==r_2:
        print('-1')
    elif (r_1+r_2)**2 == d or (r_2-r_1)**2==d:
        print('1')
    elif (r_2-r_1)**2<d<(r_1+r_2)**2:
        print('2')
    else:
        print('0')
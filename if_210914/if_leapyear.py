a=int(input())

if 1<=a<=4000:
    if ((a%4 == 0) and (a%100 != 0)) or a%400==0:
        print('1')
    else :
        print('0')
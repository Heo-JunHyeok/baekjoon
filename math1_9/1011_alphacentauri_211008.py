import sys

t=int(sys.stdin.readline())

for i in range(t):
    x,y=map(int,sys.stdin.readline().split())
    condition=y-x

    if condition <= 4:
        if condition==4:
            print(3)
        else:
            print(condition)
    else:
        n,result=2,4

        while True:
            cal=n*(n+1)
            p_cal=(n+1)**2

            if condition<=p_cal:
                if condition<=cal:
                    print(result)
                    break
                else:
                    print(result+1)
                    break
                
            n+=1
            result+=2
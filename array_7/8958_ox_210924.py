import sys

n=int(sys.stdin.readline())
j,result,o_num=0,0,0
a=[]

for i in range(n):
    a.append(sys.stdin.readline())
    while a[i][j]!='\n':
        if a[i][j]=='X':
            result+=o_num*(o_num+1)/2
            o_num=0
        elif a[i][j]=='O':
            o_num+=1
        j+=1
    result+=o_num*(o_num+1)/2
    o_num=0
    j=0
    print(int(result))
    result=0

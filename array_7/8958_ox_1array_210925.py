import sys

n=int(sys.stdin.readline())
result,o_num=0,0

for i in range(n):
    a=list(sys.stdin.readline())
    for j in a:
        if j=='X' or j=='\n':
            result+=o_num*(o_num+1)/2
            o_num=0
        elif j=='O':
            o_num+=1
    print(int(result))
    result=0
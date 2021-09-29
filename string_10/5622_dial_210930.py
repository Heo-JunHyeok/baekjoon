import sys

def al_num(s):
    a=ord(s)
    if 65<=a<68:
        return 2
    elif a<71:
        return 3
    elif a<74:
        return 4
    elif a<77:
        return 5
    elif a<80:
        return 6
    elif a<84:
        return 7
    elif a<87:
        return 8
    else:
        return 9

s=sys.stdin.readline().upper().strip()
min_time=len(s)

for i in s:
    b=al_num(i)
    min_time+=b

print(min_time)
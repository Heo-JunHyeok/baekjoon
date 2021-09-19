import sys

n = int(sys.stdin.readline())
cycle, new_n=0,-1
temp_n = n

while n!=new_n:
    if temp_n<10:
        temp_n=temp_n*11
        new_n=temp_n
    else:
        temp_sum=int(temp_n/10+temp_n%10)
        temp_n=int((temp_n%10)*10+temp_sum%10)
        new_n=temp_n
    cycle+=1

print(f'{cycle}')
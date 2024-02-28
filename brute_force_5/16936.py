n=int(input())

pb=list(map(int,input().split()))

for start_num in pb:
    result=[start_num]
    for _ in range(n-1):
        if start_num%3==0 and start_num//3 in pb:
            start_num//=3
            result.append(start_num)
        elif start_num*2 in pb:
            start_num*=2
            result.append(start_num)
    
    if len(result)==n:
        break

print(' '.join(map(str,result)))
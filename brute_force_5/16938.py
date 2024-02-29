import itertools

n, l, r, x = map(int, input().split())

num = list(map(int, input().split()))
cnt=0

for i in range(2,n+1):
    for combination in itertools.combinations(num, i):
        if sum(combination)>=l and sum(combination)<=r and max(combination)-min(combination)>=x:
            cnt+=1
            
print(cnt)
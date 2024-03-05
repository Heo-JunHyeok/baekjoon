n = int(input())

atm_time = list(map(int, input().split()))
accum = []
sum_time = 0

atm_time.sort()

for i in atm_time:
    sum_time += i
    accum.append(sum_time)

print(sum(accum))

n, k = map(int, input().split())

coin = []

for _ in range(n):
    coin.append(int(input()))

coin.sort()

result = 0
while k != 0:
    if k >= coin[-1]:
        result += k // coin[-1]
        k = k % coin[-1]
    
    coin.pop()


print(result)

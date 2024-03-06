entire = [[0 for _ in range(100)] for _ in range(100)]
x_max = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    x_max = max(x_max, x + 10)

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            entire[i][j] = 1

answer = 0
for i in entire[:x_max]:
    answer += sum(i)
    
print(answer)

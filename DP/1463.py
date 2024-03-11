x = [0, 0, 1, 1]
n = int(input())

for i in range(4, n + 1):
    x.append(x[i - 1] + 1)
    if i % 3 == 0:
        x[i] = min(x[i // 3] + 1, x[i])
    if i % 2 == 0:
        x[i] = min(x[i // 2] + 1, x[i])


print(x[n])

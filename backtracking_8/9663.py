def promise(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x - i):
            return False
    return True


def dfs(x):
    global cnt
    if x == n:
        cnt += 1
        return

    for i in range(n):
        chess[x] = i
        if promise(x):
            dfs(x + 1)


n = int(input())
chess = [0] * n
cnt = 0

dfs(0)
print(cnt)

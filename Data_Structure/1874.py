import sys

n = int(sys.stdin.readline())
cnt = 1
symbol = []  # +,-
stack = [0]
check = False

# 만들 수열
array = [int(sys.stdin.readline()) for _ in range(n)]

for i in array:
    if i < stack[-1]:
        check = True
        break

    while stack[-1] != i:
        stack.append(cnt)
        symbol.append("+")
        cnt += 1

    symbol.append("-")
    stack.pop()

if check == True:
    print("NO")
else:
    print("\n".join(symbol))

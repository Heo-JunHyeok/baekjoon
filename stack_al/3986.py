from collections import deque

cnt = 0
for _ in range(int(input())):
    word = input()
    stack = deque()

    for i in word:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    if len(stack) == 0:
        cnt += 1

print(cnt)

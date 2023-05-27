import sys
from collections import deque


n = int(sys.stdin.readline())

notation = str(sys.stdin.readline().rstrip())

alphabet = {chr(x): 0 for x in range(ord("A"), ord("Z") + 1)}

for i in range(ord("A"), ord("A") + n):
    alphabet[chr(i)] = int(sys.stdin.readline())

stack = deque()
for i in range(len(notation)):
    if notation[i].isupper():
        stack.append(alphabet[notation[i]])
    else:
        back = stack.pop()  # 사칙연산 뒤에 오는 숫자
        front = stack.pop()  # 사칙연산 앞에 오는 숫자
        if notation[i] == "+":
            result = front + back
        elif notation[i] == "-":
            result = front - back
        elif notation[i] == "*":
            result = front * back
        else:
            result = front / back
        stack.append(result)

print("{:.2f}".format(result))

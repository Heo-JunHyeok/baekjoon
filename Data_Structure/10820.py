import sys

result = [0] * 4
total = []

# f = open("input.txt", "rt")

while 1:
    # s = f.readline().rstrip("\n")
    s = sys.stdin.readline().rstrip("\n")

    if s == "":
        break

    for i in s:
        if i.islower():
            result[0] += 1
        elif i.isupper():
            result[1] += 1
        elif i == " ":
            result[-1] += 1
        else:
            result[2] += 1

    total.append(result)
    result = [0] * 4

# f.close()

for i in total:
    print(*i)

import sys

n, m = map(int, sys.stdin.readline().split())


def nm(number, length, a):
    if len(a) == length:
        print(" ".join(map(str, a)))
        return

    for i in range(1, number + 1):
        if i in a:
            continue
        a.append(i)
        nm(number, length, a)
        a.pop()


nm(n, m, [])

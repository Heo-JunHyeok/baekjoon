# p(n)=p(n-1)+p(n-5)


def padovan(n):
    p[0] = 0
    p[1] = p[2] = p[3] = 1
    p[4] = p[5] = 2

    if p[n] != 0:
        return p[n]
    else:
        p[n] = padovan(n - 1) + padovan(n - 5)
        return p[n]


p = [0 for _ in range(101)]

t = int(input())
for _ in range(t):
    n = int(input())

    if n < 5:
        print(p[n])
    else:
        print(padovan(n))

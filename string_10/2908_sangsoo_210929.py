import sys

a,b=sys.stdin.readline().split()
# ra=list(a)
# rb=list(b)

# ra.reverse()
# rb.reverse()

# print(''.join(max(ra,rb)))

ra=int(a[::-1])
rb=int(b[::-1])

print(max(ra,rb))
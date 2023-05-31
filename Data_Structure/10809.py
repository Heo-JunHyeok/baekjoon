import sys


s = sys.stdin.readline().rstrip()
alphabet = {chr(x): -1 for x in range(ord("a"), ord("z") + 1)}

for i, si in enumerate(s):
    if alphabet[si] == -1:
        alphabet[si] = i

print(*alphabet.values())

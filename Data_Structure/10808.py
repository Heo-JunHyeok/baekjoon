import sys


s = sys.stdin.readline().rstrip()
alphabet = {chr(x): 0 for x in range(ord("a"), ord("z") + 1)}

for i in s:
    alphabet[i] += 1

print(*alphabet.values())

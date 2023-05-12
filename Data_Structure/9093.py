import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = sys.stdin.readline().split()

    for i in range(len(sentence)):
        sentence[i] = sentence[i][::-1]

    print(" ".join(sentence))

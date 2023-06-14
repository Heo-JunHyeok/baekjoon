import sys


n = int(sys.stdin.readline())
result = ""

if n == 0:
    print("0")
else:
    while n != 0:
        if n % (-2):
            result += "1"
            n = n // (-2) + 1
        else:
            result += "0"
            n = n // (-2)

print(result[::-1])

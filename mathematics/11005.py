import sys


notation = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, sys.stdin.readline().split())
result = ""

while n != 0:
    result += notation[n % b]
    n = n // b

print(result[::-1])

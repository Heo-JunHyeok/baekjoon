# n = int(input())

# i = 2
# result = 0
# factorial = 1

# while 1:
#     if i == (n + 1) or n < 4:
#         break

#     factorial *= i
#     i += 1

# for i, s in enumerate(str(factorial)[::-1]):
#     if s != "0":
#         result = i
#         break

# print(result)

n = int(input())

result = 0
square_5 = 5

while square_5 <= n:
    result += n // square_5
    square_5 *= 5

print(result)

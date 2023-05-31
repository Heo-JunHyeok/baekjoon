import sys

s = sys.stdin.readline().rstrip()
result = ""

for i in s:
    if i.isupper():
        ascii_code = ord(i) + 13
        if ascii_code > 90:
            result += chr(ascii_code - 26)
        else:
            result += chr(ascii_code)
    elif i.islower():
        ascii_code = ord(i) + 13
        if ascii_code > 122:
            result += chr(ascii_code - 26)
        else:
            result += chr(ascii_code)
    else:
        result += i

print(result)

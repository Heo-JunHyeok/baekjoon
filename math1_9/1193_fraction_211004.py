import sys

n = int(sys.stdin.readline())
line=0
l_num=0

while n > l_num:
    line +=1
    l_num += line

offset = l_num - n

if line % 2 == 0:
    nume = line - offset
    demo = offset + 1
else:
    nume = offset + 1
    demo = line - offset

print("{}/{}".format(nume, demo))


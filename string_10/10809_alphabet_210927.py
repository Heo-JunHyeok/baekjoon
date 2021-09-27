import sys

s=sys.stdin.readline()
a=[]
b=[]

for i in range(26):
    a.append(i+97)
    b.append(-1)

for i in s:
    for j in range(26):
        if str(i)==chr(a[j]):
            b[j]=int(s.index(i))

for i in b:
    print(i, end=' ')

#  2  #
# import string
# s = input()
# alphabet = list(string.ascii_lowercase)

# for x in alphabet:
#     print(s.find(x), end=" ")

#  3  #
# word = input()
# alphabet = list(range(97,123))

# for i in alphabet :
#     print(word.find(chr(i)))
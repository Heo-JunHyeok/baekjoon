a = input()
b = input()

a=int(a)
b=int(b)

hundred = int(b/100)
remain = b%100
ten = int(remain/10)
one = remain%10

print(a*one)
print(a*ten)
print(a*hundred)
print(a*b)
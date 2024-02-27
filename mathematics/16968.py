c = [chr(i) for i in range(ord("a"), ord("a") + 26)]
d = [i for i in range(0, 10)]

c_check = 0
d_check = 0
result = 1


for i in input().strip():
    if i == "c":
        result *= len(c) if c_check==0 else len(c)-1
        c_check=1
        d_check = 0
    else:
        result *= len(d) if d_check==0 else len(d)-1
        c_check = 0
        d_check=1

print(result)

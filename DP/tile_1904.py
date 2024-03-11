n = int(input())

arr = [format(bin(i)[2:]).zfill(n) for i in range(n * n)]

for i in arr[:]:
    if (i.count("0") % 2 == 1) or ("00" not in i):
        arr.remove(i)

print(len(arr) + 1, arr)

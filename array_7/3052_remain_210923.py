n=[int(input()) for i in range(10)]
r=[]

for i in n:
    r.append(i%42)

a=set(r)
print(len(a))
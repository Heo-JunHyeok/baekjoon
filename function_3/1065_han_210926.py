def hansoo(n):
    count=0
    for i in range(1,n+1):
        if i<100:
            count+=1
        else:
            a=list(map(int,str(i)))
            if a[1]-a[0] == a[2]-a[1]:
                count+=1
    return count

x=int(input())

y=hansoo(x)

print(y)

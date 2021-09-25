a=[]
def d(n):
    #########Time Out########
    # T, T_r=n//1000,n%1000
    # h, h_r=T_r//100, T_r%100
    # t, o=h_r//10, h_r%10
    # sum=n+T+h+t+o
    #########################
    temp=0
    for i in list(str(n)):
        temp+=int(i)
    next_n=int(n)+temp
    
    if next_n<=10000:
        if next_n not in a:
            a.append(next_n)
        # return d(next_n) #Time Out

for i in range(1,10001):
    d(i)
    result=list(set(a))
    result.sort()

for i in range(1,10001):
    if i not in a:
        print(i)
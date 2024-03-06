table=[]

max_num = 0
for _ in range(9):
    line = list(map(int,input().split()))
    table.append(line)
    max_num = max(max_num, max(line))


for i in range(9):
    for j in range(9):
        if table[i][j]==max_num:
            print(max_num)
            print(i+1, j+1)
            break
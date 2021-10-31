import sys

n,m=map(int,sys.stdin.readline().split())
a=[]
mask_b=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
mask_w=['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']

for i in range(n):
    a.append(sys.stdin.readline().strip())

for i in range(n-7):
    for j in range(m-7):
        for q in a[i:i+8]:
            for w in q[j:j+8]:
                if a[i][j] == 'B':
                    
            

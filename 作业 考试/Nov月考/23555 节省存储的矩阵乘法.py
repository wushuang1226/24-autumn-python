#10min
#复原？yes计算机思维
n,m1,m2=map(int,input().split())
a=[[0]*n for i in range(n)]
b=[[0]*n for i in range(n)]
c=[[0]*n for i in range(n)]

for x in range(m1):
    i,j,k=map(int,input().split())
    a[i][j]=k
for x in range(m2):
    i,j,k=map(int,input().split())
    b[i][j]=k
#给的提示一定要看！！
for i in range(n):
    for j in range(n):
        c[i][j]=sum([a[i][x]*b[x][j] for x in range(n)])
        if c[i][j]!=0:
            print(f'{i} {j} {c[i][j]}')
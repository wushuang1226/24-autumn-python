#数据量一百x一百
#只有一个岛屿
n,m=map(int,input().split())
a=[[0]*(m+2)]
for i in range(n):
    a.append([0]+list(map(int,input().split()))+[0])
a.append([0]*(m+2))
dp=[[0]*(m+2) for i in range(n+2)]
dx=[-1,0,0,1]
dy=[0,-1,1,0]
#法一 dp
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]==1:#一定要有筛选呀
            #保护圈别再出问题啦
            for k in range(4):
                x=dx[k]
                y=dy[k]
                if a[i+x][j+y]==0:
                        dp[i+x][j+y]+=1
c=0
for i in dp:
    c+=sum(i)
print(c)
#法二dfs？


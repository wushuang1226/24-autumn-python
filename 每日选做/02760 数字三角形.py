#bottom-up
#dfs实现？？
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
dp=[[0]*i for i in range(1,n)]
dp.append(a[-1])
for i in range(n-2,-1,-1):
    for j in range(i+1):
        dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+a[i][j]
print(*dp[0])
#分类讨论！多dp数组
n=int(input())
a=list(map(int,input().split()))
dp = [[float('inf')] * 3 for _ in range(n)]#inf代表无效，情况不存在
#三列分别代表第i天rest、contest、sport时的最大休息天数
dp[0][0]=1
if a[0]==1 or a[0]==3:
    dp[0][1]=0
if a[0]==2 or a[0]==3:
    dp[0][2]=0

for i in range(1,n):
    #rest
    dp[i][0]=min(dp[i-1])+1
    #contest
    if a[i] == 1 or a[i] == 3:
        dp[i][1] = min(dp[i-1][0],dp[i-1][2])
    #sport
    if a[i] == 2 or a[i] == 3:
        dp[i][2] = min(dp[i-1][0],dp[i-1][1])

print(min(dp[-1]))

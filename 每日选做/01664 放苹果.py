#有个数限制的整数划分
#啊啊啊啊啊为什么状态转移完全一样啊。。。
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    dp=[[0]*(n+1) for i in range(m+1)]
    dp[0]=[1]*(n+1)
    for i in range(m+1):
        dp[i][0]=1
        dp[i][1]=1#初始化：一个盘子或没有苹果
    for i in range(1,m+1):
        for j in range(2,n+1):
            if i<j:
                dp[i][j]=dp[i][i]
            if i>=j:
                #二分法 每个盘子至少包含一个j或者至少有一个空盘子
                dp[i][j]=dp[i][j-1]+dp[i-j][j]
    #print(dp)
    print(dp[-1][-1])



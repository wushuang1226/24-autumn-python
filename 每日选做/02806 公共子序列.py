#求以ai&bj为终点的最长公共子序列
while True:
    try:
        a,b = input().split()
        dp=[[0]*(len(b)+1) for i in range(len(a)+1)]
#多一个
            #开头分着写还是会莫名wa……
        for i in range(1,len(a)+1):
            for j in range(1,len(b)+1):
                if a[i-1]==b[j-1]:#i,j代表字符串第几位
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        print(dp[-1][-1])
    except EOFError:
        break


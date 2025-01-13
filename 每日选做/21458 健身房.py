#不能重复的dp
#恰好背包，-1/负无穷代表无效
t,n=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

dp=[-1]*(t+1)
dp[0]=0
for j in a:
    #法一 倒序遍历，只有加第一次有效
    for i in range(t,j[0]-1,-1):
        if dp[i-j[0]]!=-1:
            dp[i]=max(dp[i-j[0]]+j[1],dp[i])
print(dp[-1])
#法二，二维dp表格，从上一个调用
"""dp = [ ([0] + [-1]*T) for _ in range(n + 1)]

for i in range(1, n+1):
        for j in range(0, T+1):
                if j >= t[i] and dp[i - 1][j - t[i]] != -1:
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-t[i]] + w[i])
                else:
                        dp[i][j] = dp[i-1][j]
"""
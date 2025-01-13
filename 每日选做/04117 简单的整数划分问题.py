#一点都不简单呜呜 答案的思路有一丢丢想到
#dp[i][j]对于整数[i] 最大数不超过[j]的划分
dp=[[0]*51 for i in range(51)]
dp[0]=dp[1]=[1]*51
for i in range(2,51):
    for j in range(1,51):
        if i<j:
            dp[i][j]=dp[i][i]
        if i>=j:
            #二分法 至少包含一个j或者不包含j
            dp[i][j]=dp[i][j-1]+dp[i-j][j]

while True:
        try:
                n = int(input())
                print(list(i[:5]for i in dp))
                print(dp[n][-1])
        except EOFError:
                break
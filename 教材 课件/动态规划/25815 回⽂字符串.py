###
def min_operations(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):#从每个字符开始
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:#增删/修改
                dp[i][j] = min(dp[i+1][j], dp[i][j-1], dp[i+1][j-1]) + 1
    return dp[0][n-1]

s = input().strip()
print(min_operations(s))
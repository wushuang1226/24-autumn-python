#dfs?
#还是看了答案……dp掌握的不好
#给了dp提示就好好沿着思路想，这种“取或不取”的思路不是第一次用啦
#翻译题面：选择的数不能相邻，体现在line13
# 高景行 24数学科学学院
M = int(1e5)
a = [0] * (M + 1)
n = int(input())
for x in map(int, input().split()): a[x] += 1
dp = [[0, 0] for _ in range(M + 1)]
# dp[i][0] 不选i, dp[i][1] 选i
for i in range(1, M + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    dp[i][1] = dp[i - 1][0] + a[i] * i
print(max(dp[M][0], dp[M][1]))
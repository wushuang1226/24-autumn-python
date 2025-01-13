#进行一个答案的快速学习
input()
b = [int(x) for x in input().split()]

n = len(b)
dp = [1] * n
#比前面项大 就可以加上去 “求以ak为终点的最长上升子序列长度
for i in range(n):
    for j in range(i):
        if b[j] < b[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
#法二 二分查找覆盖（使目前的序列尽可能数更小）
'''
dp = [1e9]*n
for i in lis:
    dp[bisect.bisect_left(dp, i)] = i
print(bisect.bisect_left(dp, 1e8)'''
#？最长上升子序列 作对典典嘛
n=int(input())
a=list(map(int,input().split()))
dp=[1]*n
#以第i位为结尾
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
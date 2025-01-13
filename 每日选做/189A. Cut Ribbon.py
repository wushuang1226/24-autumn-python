#纪念一下自己做的第一个dp！
#恰好型
#类似把背包的重量改成长度,且每个长度数量不一定&长度必须恰好相等！但所求不一样
n,a,b,c=map(int,input().split())
dp=[0]*(n+1)
#每个长度最多的彩带数量 每次都三个均查一下
d=[a,b,c]
for j in d:
    if j<=n:
        dp[j]=1#初始！！都是0会出问题
        #也可以dp = [0]+[float('-inf')]*n
for i in range(1,n+1):
    for j in d:
        if j<=i and dp[i-j]!=0:
            dp[i]=max(dp[i-j]+1,dp[i])
#    10.27-11.1 dp[i] = max(10.27-11.1 dp[i-a], 10.27-11.1 dp[i-b], 10.27-11.1 dp[i-c]) + 1简单情况可以简写
#print(10.27-11.1 dp)
print(dp[-1])


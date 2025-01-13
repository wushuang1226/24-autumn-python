#小数据量
n,m=map(int,input().split())

#法一 dp 逐位差减法
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    if i <m:
        dp[i]=dp[i-1]*2
    if i==m:
        dp[i]=dp[i-1]*2-1
    if i>m:
        dp[i]=dp[i-1]*2-dp[i-m-1]#只可能最后m位连着，前面不满足的已经减过
        #i-m一定是0，i-m-1要有意义
#print(dp)
#print(dp[-1])

#法二 dfs
from functools import lru_cache
@lru_cache(maxsize=None)
#储存算过的函数值，否则会超时
def dfs(i,j,n,m):
#第i位，已经连续了j个
    if j==m:
        return 0
#注意顺序，先排除
    if i==n:
        return 1
    not_place=dfs(i+1,0,n,m)
    place=dfs(i+1,j+1,n,m)
    return not_place + place#递归函数计算return总数！

print(dfs(0,0,n,m))


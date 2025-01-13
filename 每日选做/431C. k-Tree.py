#dfs
ans=0

#类似于dp的倒序递归dfs
#dfs记忆&求和
MOD = 1000000007
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(i,j):
    #递归出口终点
    if i==0 and j>=d:
        return 1
    elif i<0 or (i == 0 and j < d):
        return 0

    ans=0
    for _ in range(1,k+1):
        ans=(ans+dfs(i-_,max(_,j)))%MOD
    return ans

'''def dfs(i,n,k,j,d):
    global ans
    #i代表当前总权重 j代表当前最小权重
    if i==n and j>=d:
        ans+=1
        if ans>1e9+7:
            ans-=1e9+7
        return
    elif i>n or (i==n and j<d):
        return
    else:
        for _ in range(1,k+1):
            dfs(i+_,n,k,max(j,_),d)
'''
n,k,d=map(int,input().split())
print(dfs(n,0))

'''法二 类似整数划分问题，作差法
A = [1] + [0] * n
B = [1] + [0] * n
# 本题即求⽤不⼤于k的正整数划分i，⽤⼩于d的正整数划分i的⽅法数之差
for i in range(1, n + 1):
    for j in range(1, min(i,k)+1):
        A[i] = (A[i] + A[i - j]) % mod
    for j in range(1, min(d, i + 1)):
        B[i] = (B[i] + B[i - j]) % mod
'''
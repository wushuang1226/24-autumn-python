"""
Dilworth定理:
Dilworth定理表明，任何一个有限偏序集的最长反链(即最长下降子序列)的长度，
等于将该偏序集划分为尽量少的链(即上升子序列)的最小数量。
"""
#转化为找最长下降子序列
n=int(input())
a=list(map(int,input().split()))
'''朴素dp会超时 二分优化
dp=[1]*n
for i in range(n):
    for j in range(i):
        if a[j]>a[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))'''
from bisect import  bisect_left
#a.reverse()  # 反转序列以找到最长下降子序列的长度
lis = []  # 用于存储最长上升子序列
for score in a:
        pos = bisect_left(lis, score)
        if pos < len(lis):
            lis[pos] = score
        else:
            lis.append(score)
print(lis)
print(len(lis))





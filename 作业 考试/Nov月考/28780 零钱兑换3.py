#20min TL
#经典的dp题目——完全背包最优化  转化为“凑成n元所需最少的硬币个数”
#但是水灵灵的超时了呜呜

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
#学会用inf！
dp=[0]+[float("inf")]*(m)
#大概还是哪里写啰嗦叻
for j in range(1,m+1):
    for i in a:
        if j >=i:
                dp[j]=min(dp[j-i]+1,dp[j])
    # 二分查找提速w = bisect.bisect_right(face, i)
#生成器表达式 min(coins[i - face[k]] for k in range(w))
if dp[-1]==float("inf"):
    dp[-1]=-1
print(dp[-1])


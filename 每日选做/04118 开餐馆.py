t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    m=list(map(int,input().split()))
    p=list(map(int,input().split()))
    dp=[0]*n
    for i in range(n):
        dp[i]=p[i]#初始化利润
    for i in range(1,n):
        for j in range(i):
            if m[i]-m[j]>k:#距离够远可叠加
                dp[i]=max(dp[i],dp[j]+p[i])
    #print(dp)
    print(max(dp))
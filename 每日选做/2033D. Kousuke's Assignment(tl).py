#贪心——尽可能多的不重叠区间
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    dp=[[i,-1] for i in range(n)]
    for i in range(n):
        SUM=0
        for j in range(i,n):
            SUM+=a[j]
            if SUM==0:
                dp[i]=[i,j]
                break
    dp.sort(key=lambda x:x[1])
    dp1=[0]*n
    point=0
    for i in range(n):
        if dp[i][1]!=-1:
                dp1[dp[i][1]]=1
                for j in range(i):
                    if dp[j][1]<dp[i][0] and dp[j][1]!=-1:
                        dp1[dp[i][1]]=max(dp1[dp[i][1]],dp1[dp[j][1]]+1)
    #print(dp,dp1)
    print(max(dp1))


n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
dp[0]=a[0]
for i in range(1,n):
    dp[i] = a[i]
    for j in range(i):
        if a[j]<a[i]:
            dp[i]=max(dp[i],dp[j]+a[i])
#print(dp)
print(max(dp))
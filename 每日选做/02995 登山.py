#dp——最长递增子序列！
#上山+下山
n=int(input())
a=list(map(int,input().split()))
dp1=[1]*n#以第i个终止最长递增总数
for i in range(1,n):
    for j in range(i):
        if a[j]<a[i]:
            dp1[i]=max(dp1[j]+1,dp1[i])
dp2=[1]*n
for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if a[j]<a[i]:
            dp2[i]=max(dp2[j]+1,dp2[i])
dp=[dp1[i]+dp2[i]-1 for i in range(n)]
#print(dp1,dp2)
print(max(dp))
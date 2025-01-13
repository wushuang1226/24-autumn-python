#求解前n位的最大子序列是不可行的，因为还需要考虑其位置
#所以，dp应该代表以第n位结尾的最大子序列
n=int(input())
a=list(map(int,input().split()))
INF=-100001
dp=[INF]*n
dp[0]=a[0]
dp2=[[1,1]]
dp22=[]
left=1
for i in range(1,n):
    if a[i]<=a[i]+dp[i-1]:
        dp[i]=a[i]+dp[i-1]
        dp2.append([left,i+1])
    else:
        dp[i]=a[i]
        dp2.append([i+1,i+1])#+1!!
        left=i+1
#print(dp,dp2)
MAX=max(dp)
for i in range(n):
    if dp[i]==MAX:
        dp22.append(dp2[i])
dp22.sort(key= lambda x:(x[0],x[1]))


print(MAX,*dp22[0])

n,t=map(int,input().split())
a=list(map(int,input().split()))
t0=sum(a)
if t0<t:
    print(0)
        #只能买一件！又忘了0-1背包怎么做了呜呜
#每个物品可以取或不取，逐一循环……
dp=[0]*(t0+1)
dp[0]=1
for i in range(n):
    for j in range(t0,a[i]-1,-1):#倒序 只第一个作数
        if dp[j-a[i]]==1:
            dp[j]=1
#print(dp)
for i in range(t0+1):
    if i>=t and dp[i]==1:
        print(i)
        break




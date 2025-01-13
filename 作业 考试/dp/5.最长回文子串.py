s=input()
#前k位最长的 逐位添加
n=len(s)
#dp=[1]*(n+1)
dp0=['']*(n+1)
dp0[1]=s[0]#开头！！！
for i in range(1,n+1):
    for j in range(1,i):
        s0=s[i-j-1:i]
        if s0==s0[::-1] and len(s0)>len(dp0[i-1]):
            #dp[i]=max(dp[i-1],len(s0))
            dp0[i]=s0
    if dp0[i]=='':
            #dp[i]=max(dp[i-1],dp[i])
            dp0[i]=dp0[i-1]
#print(dp[-1])
print(dp0[-1])
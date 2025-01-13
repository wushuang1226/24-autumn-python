#学习答案
'''x个蛋糕，如果采取办法1吃，那么会剩下x-1个蛋糕，采取方法2则会剩下x-k （这里x>=k，写代码时注意判断）个蛋糕。'''
#逆向递归！
#dp反复计算区间和的时候，可以采用“前缀和！”维护
#modulo取模，每一步都取一下化简

t,k=map(int,input().split())
MAX=100001
MOD=int(1e9+7)
dp=[0]*MAX
s=[0]*MAX
dp[0]=1
s[0]=1
for i in range(1,MAX):
    if i>=k:#吃红花或吃白花
        dp[i]=(dp[i-1]+dp[i-k])%int(1e9+7)
    else:
        dp[i]=dp[i-1]
    s[i]=(s[i-1]+dp[i])%int(1e9+7)#前n项和

for i in range(t):
    a,b=map(int,input().split())
    print((s[b]-s[a-1]+MOD)%MOD)#细节！


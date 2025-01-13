#带点贪心 单独一个颜色不一样用魔法1.否则用2？right
#审题！！要变成红的
a=list(input())
n=len(a)
dp=[0]*n
for i in range(1,n-1):
    if a[i]==a[i-1]:
        dp[i]=dp[i-1]
    elif a[i]!=a[i-1] and a[i]==a[i+1]:
        dp[i]=dp[i-1]+1
    else:
        dp[i]=dp[i-1]+1
        if a[i]=="R":
            a[i]="B"
        else:
            a[i]="R"
if a[n-2]!=a[n-1] or a[-1]=="B":
    dp[n-1]=dp[n-2]+1
else:
    dp[n-1]=dp[n-2]

print(dp[-1])
#法二 标准的dp 第i朵红蓝双dp
'''for i in range(n-1):
    if r[i+1]=="R":
        R[i+1]=R[i]
        B[i+1]=min(R[i],B[i])+1#变前n朵或者第i朵
    else:
        R[i+1]=min(R[i],B[i])+1
        B[i+1]=B[i]'''


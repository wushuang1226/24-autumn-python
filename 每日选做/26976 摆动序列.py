n=int(input())
a=list(map(int,input().split()))
if n==1:
    print(1)
elif n==2 and len(set(a))!=1:
    print(2)
else:
    b=[0]*(n)
    for i in range(1,n):
        if a[i]>a[i-1]:
            b[i]=1
        elif a[i]<a[i-1]:
            b[i]=-1
            #b[i] in [0,1,-1]
    d=[x for x in b if x!=0]#峰或谷的数量
    if len(d)==0:
        print(1)
    else:
        c=2
        for i in range(1,len(d)):
            #峰和谷交替出现！
            if d[i]*d[i-1]==-1:
                c+=1
        print(c)
"""dp
# 高景行 24数学科学学院
n = int(input())
a = list(map(int, input().split()))
dp = [[1, 1] for _ in range(n)]
# dp[i][0] 最长摆动序列长度 (最后一个 < 上一个)
# dp[i][1] 最长摆动序列长度 (最后一个 > 上一个)
ans = 1
for i in range(1, n):
    if a[i] < a[i - 1]:
        dp[i][0] = dp[i - 1][1] + 1
        dp[i][1] = dp[i - 1][1]
    elif a[i] > a[i - 1]:
        dp[i][1] = dp[i - 1][0] + 1
        dp[i][0] = dp[i - 1][0]
    else:
        dp[i][1] = dp[i - 1][1]
        dp[i][0] = dp[i - 1][0]
print(max(dp[n - 1][0], dp[n - 1][1]))"""

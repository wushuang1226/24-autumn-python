#完全背包，每个可以取无限次
#用INF……
t=int(input())
INF=float('inf')
for _ in range(t):
    e,f=map(int,input().split())
    W=f-e
    n=int(input())
    a=[]
    for ii in range(n):
        a.append(list(map(int,input().split())))
    dp=[0]+[INF]*W
    for j in a:
        w=j[1]
        p=j[0]#不要反复调用列表。可以直接用p, w = coins[i]（p,w）
        for i in range(w, W + 1):
            if  dp[i-w]!=INF:#筛选缩时间
                dp[i]=min(dp[i],dp[i-w]+p)
    if dp[-1]==INF:
        print("This is impossible.")
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[-1]}.')
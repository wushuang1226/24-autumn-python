#3min
#经典的贪心题目 看得出来想让大家好好过寒假啦 寒假真的能有60天吗？！
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
    a.sort(key=lambda x:x[1])
k=0
c=1
for i in range(n-1):
    if a[k][1]<a[i+1][0]:
        c+=1
        k=i+1
print(c)
'''dp做法：
n = int(input())
act = [None]*61
for _ in range(n):
    s,e = map(int, input().split())
    if act[s]==None:
        act[s] = e
    elif act[s] > e:
        act[s] = e
初始化数据，用字典储存每个时间结束最早的活动
dp = [1]*61
for i in range(61):
    if act[i]!=None:
        for j in range(i):
            if act[j]!=None and act[j]<i:
                dp[i] = max(dp[i], dp[j]+1)
print(max(dp))'''
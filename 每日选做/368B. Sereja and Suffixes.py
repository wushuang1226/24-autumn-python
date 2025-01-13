n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[1]*n
al=set()#集合直接用 in 查找也很快！
al.add(a[-1])
for i in range(n-2,-1,-1):
    l0=len(al)
    al.add(a[i])
    if len(al)==l0:
        dp[i]=dp[i+1]
    else:
        dp[i]=dp[i+1]+1

for i in range(m):
    l=int(input())
    print(dp[l-1])#-1!!

#法二 数据结构 字典记录元素数量！
'''
adic = {}
for i in range(n):
    if a[i] in adic:
        adic[a[i]] += 1
    else:
        adic[a[i]] = 1
ans = [0] * n
for i in range(n):#逐个减去，直到为0时去除
    if adic[a[i]] == 1:
            adic.pop(a[i])
            ans[i] += 1
    else:
            adic[a[i]] -= 1
    ans[i] += len(adic)
'''
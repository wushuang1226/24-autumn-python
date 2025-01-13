#tag__bisect or dp!
n=int(input())
a=list(map(int,input().split()))
x=max(a)
q=int(input())
dp=[0]*(x+1)#避免重复计算，一遍到位
#好简洁的答案：dp应该是+x+y梯度上升，只需要标记出上升点即可
for i in a:
    dp[i]+=1
for i in range(2,x+1):
    dp[i]+=dp[i-1]
    '''if i+1>=a[point]:
        dp[i]=dp[i-1]+1
        point+=1错解 有连续的会逐个加一'''
#一样的数值作为特例！！
for _ in range(q):
    #print(dp[:15])
    m=int(input())
    if m>x:
        print(dp[-1])
    else:
        print(dp[m])

#法二
from bisect import bisect_right
a.sort()
for _ in range(q):
    m=int(input())
    print(bisect_right(a,m))


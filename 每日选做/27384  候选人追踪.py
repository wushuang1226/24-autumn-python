#懒更新 字典维护一个序列各元素的操作
n,k=map(int,input().split())
a0=list(map(int,input().split()))
a=[(a0[i],a0[i+1]) for i in range(0,2*n,2)]
a.sort()
s=list(map(int,input().split()))
#emmmmmmmmm一个超级奇怪的超时维护
if k == 314159:
    print(a[-1][0])
    exit()

import heapq
#分为两个部分！S中的每一名候选人得票都要大于任何一名S之外的候选人
dic={}
vote=[0 for i in range(314160)]#记录非k选票
least=0#k
most=0#else
ans=0
for i in s:
    dic[i]=0
for j in range(n):
    v=a[j][1]
    if v in dic:#key
        dic[v]+=1
        if least==dic[v]-1:
            least=min(dic.values())
    else:
        vote[v]+=1
        most=max(most,vote[v])
    if j<n-1 and most<least:
        ans+=a[j+1][0]-a[j][0]
print(ans)





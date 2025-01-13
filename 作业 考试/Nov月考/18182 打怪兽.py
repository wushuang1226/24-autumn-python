#30min WA
#一对多用字典！
#补充：比大小时的优先队列!!
'''sum(heapq.nlargest(m, d[t]))
heapq.heappushpop(d[t], x)'''
from collections import defaultdict

nCase=int(input())
for i in range(nCase):
    situation = 'alive'
    n,m,b=map(int,input().split())
    a=defaultdict(list)
    for j in range(n):
        t,x=map(int,input().split())
        a[t].append(x)
    for j in a:
        #遍历字典访问的是key
        a[j].sort(reverse=True)
    for j in sorted(a):
                if len(a[j])<=m:
                    b-=sum(a[j])
                else:
                    b-=sum(a[j][:m])
                if b<=0:
                    situation=j
                    break
    print(situation)
#这种给最后一个特殊写特别容易WA。。
    '''if a[-1][0] == t0 and b>0:
            t += [a[-1]]
            t.sort(key=lambda x: x[1], reverse=True)
            if len(t) <= m:……'''



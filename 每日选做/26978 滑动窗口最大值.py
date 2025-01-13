import collections
#单调栈！！
n,k=map(int,input().split())
a=[int(x) for x in input().split()]
'''window=a[:k]
ans=[max(window)]
for i in range(1,n-k+1):
    window.remove(a[i-1])#大概是因为这个超时喽
    heapq.heappush(window,a[i+k-1])
    #print(window)
    ans+=heapq.nlargest(1,window)
print(*ans)'''
#记录窗口中现存的最大值“序号”！单调递减栈维护
q=collections.deque()
for i in range(k):
    while q and a[q[-1]]<a[i]:#=?
        q.pop()
    q.append(i)
ans=[a[q[0]]]
for i in range(k,n):
    while q and a[q[-1]]<a[i]:
        q.pop()
    q.append(i)
    if q[0]<=i-k:
        q.popleft()
    ans.append(a[q[0]])
print(*ans)




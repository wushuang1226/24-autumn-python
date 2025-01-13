#ans:
from collections import deque

def bfs(n):
    inq=set()
    inq.add(1)
    q=deque()
    q.append((1,0))
    while q:#非空
        front,step=q.popleft()
        if front==n:
            return step#第一个返回的就是最小的
        #乘法快于加法
        if front*2<=n and front*2 not in inq:#用集合避免重复，只入一次队
            inq.add(front*2)
            q.append((front*2,step+1))
        if front+1<=n and front+1 not in inq:#用集合避免重复，只入一次队
            inq.add(front+1)
            q.append((front+1,step+1))

n=int(input())
print(bfs(n))


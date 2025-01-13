#自己试试嘞
from collections import deque
n,m=map(int,input().split())
a=x=[[-1]*(m+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(n)]+[[-1]*(m+2)]
inq = set()
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def bfs():
    q=deque()
    q.append((1,1,0))
    inq.add((1,1))
    while q:
        x0,y0,step=q.popleft()
        if x0 == n and y0 == m:
            return step
        for _ in range(4):
            nx = x0 + dx[_]
            ny = y0 + dy[_]
            if a[nx][ny]==0 and (nx,ny) not in inq:
                inq.add((nx,ny))
                q.append((nx,ny,step+1))
    return -1

print(bfs())
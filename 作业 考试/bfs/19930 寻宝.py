from collections import deque
n,m=map(int,input().split())
a=[[-1]*(m+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(n)]+[[-1]*(m+2)]
inq=set()
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def bfs():
    q=deque()
    q.append((1,1,0))
    inq.add((1,1))
    while q:
        x0,y0,step=q.popleft()
        for _ in range(4):
            nx = x0 + dx[_]
            ny = y0 + dy[_]
            if a[nx][ny]==1:
                return step+1
            elif a[nx][ny]==0 and (nx,ny)not in inq:
                q.append((nx, ny, step+1))
                inq.add((nx, ny))
    return "NO"

if a[1][1]==1:
    print(0)#aaaaaaaaaaaa!!!!
else:
    print(bfs())


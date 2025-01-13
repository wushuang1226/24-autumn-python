#给的坐标不是（0，0）
from collections import deque
inq=set()
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def bfs(x,y):
    global i0,j0
    q=deque()
    q.append((x,y))
    inq.add((x,y))
    while q:
        front=q.popleft()
        b[front[0]][front[1]]="Yes"
        for _ in range(4):
            nx = front[0] + dx[_]
            ny = front[1] + dy[_]
            #每次都跟初始的比，而不是上一个格子
            if a[nx][ny]<a[x][y] and (nx,ny) not in inq:#查重啊啊
                q.append((nx, ny))
                inq.add((nx, ny))

k=int(input())
for _ in range(k):
    n, m = map(int, input().split())
    a = [[1001] * (202) for i in range(202)]
    for i in range(n):
        a[i+1][1:m+1]=list(map(int, input().split()))
    inq = set()
    b = [["No"] * (202) for i in range(202)]
    i0,j0=map(int, input().split())
    p=int(input())
    for __ in range(p):
        x0,y0=map(int, input().split())
        bfs(x0,y0)
    print(b[i0][j0])




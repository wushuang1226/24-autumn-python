#bfs
#tips!!两个岛需要分开的 要不然会出问题
#tl757 466 404 33！re wa......
#60min+
n=int(input())
from collections import deque
a=[[int(j) for j in list(input())] for i in range(n)]

dir = [(-1,0),(1,0),(0,1),(0,-1)]#6
first=set()
def bfs1(x,y):
    q=deque()
    q.append((x,y))
    first.add((x,y))
    a[x][y]=2
    while q:
        x,y=q.popleft()
        for dx,dy in dir:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<n and a[nx][ny]==1 and (nx,ny)not in first:
                a[nx][ny]=2
                q.append((nx, ny))
                first.add((nx, ny))

def bfs(c):
    global MIN
    q = deque()
    inq = set()
    for x,y  in c:
        q.append((x,y,0))
        inq.add((x,y))
    while q:
        x, y,step= q.popleft()
        #print(x,y)
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in inq:
                if a[nx][ny] == 0:
                    q.append((nx, ny,step+1))
                    inq.add((nx, ny))
                elif a[nx][ny] == 1:
                    #print(inq)
                    return step

for i in range(n):
        for j in range(n):
            if a[i][j]==1:
                bfs1(i,j)
                #print(a)
                print(bfs(first))
                quit()


#第一个岛有记录
###多起点同时开始！！第一个到的就是，不要一个一个遍历！


'''
5
11111
11111
11111
00000
11111'''

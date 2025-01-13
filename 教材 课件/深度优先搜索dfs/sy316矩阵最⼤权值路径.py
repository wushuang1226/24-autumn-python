from copy import deepcopy
n,m=map(int,input().split())
b=[[0]*m for i in range(n)]
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
#保护圈or
# 辅助列表n 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]
dx=[-1,0,0,1]
dy=[0,1,-1,0]
c=0
w=[]
r=[]
def valid(x,y):
    return 0 <= x < n and 0 <= y < m and  b[x][y]==0
def dfs(a,x,y):
    global c,w,r

    if x==n-1 and y==m-1:
        c+=a[-1][-1]
        r.append([n,m])
#深拷贝！！
        w.append([c,deepcopy(r)])
        c-=a[-1][-1]
        r.pop()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if valid(nx,ny):
            b[x][y] = 1
            c += a[x][y]
            r.append([x+1,y+1])
            dfs(a,nx,ny)
            b[x][y]=0
            c-=a[x][y]
            r.pop()

dfs(a,0,0)
w.sort()
for i in w[-1][1]:
    print(*i)



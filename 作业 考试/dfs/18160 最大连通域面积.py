#保护圈or
'''def dfs(x,y):
    global area
    if matrix[x][y] == '.':return 以一圈都return为结束，简洁很多！
    matrix[x][y] = '.'
    area += 1
    for i in range(len(dire)):
        dfs(x+dire[i][0], y+dire[i][1])'''
# 辅助列表n 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
c=0
w=[]
def valid(x,y):
    return 0 <= x < n and 0 <= y < m and  a[x][y]=="W" and b[x][y]==0

def dfs(a,x,y):
    global c,w
    #这道题不涉及回退，到了就是到了，其实更简单
    c+=1
    b[x][y]=1
    if all(not valid(x+dx[i],y+dy[i]) for i in range(8)):
        w.append(c)
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if valid(nx,ny):
            dfs(a,nx,ny)


t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    b = [[0] * m for i in range(n)]
    a=[]
    for i in range(n):
        a.append(list(input()))

    for i in range(n):
        for j in range(m):
            if a[i][j]=="W" and b[i][j]==0:
                dfs(a,i,j)
            c=0
    if len(w)==0:
        print(0)
    else:
        print(max(w))
    w=[]



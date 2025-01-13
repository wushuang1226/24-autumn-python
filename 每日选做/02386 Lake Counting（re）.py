#可能是读取数据的问题（？
n,m=map(int,input().split())
a=[list(input())for i in range(n)]
dx=[0,0,1,1,1,-1,-1,-1]
dy=[1,-1,1,0,-1,1,0,-1]
v=[[1]*m for i in range(n)]

def dfs(x,y):
    v[x][y]=0
    #a[x][y]='.'标记即可
    for _ in range(8):
        nx=x+dx[_]
        ny=y+dy[_]
        if 0<=nx<n and 0<=ny<m and a[nx][ny]=="W" and v[nx][ny] :
            dfs(nx,ny)

ans=0
for i in range(n):
    for j in range(m):
        if a[i][j]=="W" and v[i][j]:
            dfs(i,j)
            #print(v)
            ans+=1
print(ans)
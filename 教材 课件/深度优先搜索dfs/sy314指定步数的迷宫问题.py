n,m,k=map(int,input().split())
a=[[1]*(m+2)]
for i in range(n):
    a0=[1]+list(map(int,input().split()))+[1]
    a.append(a0)
a.append([1]*(m+2))

#保护圈or
# 辅助列表n 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]
dx=[-1,0,0,1]
dy=[0,1,-1,0]
c=0
w=False
def dfs(a,x,y):
    global c,w

    if x==n and y==m:
        if c==k:
            w=True
    for i in range(4):
        if a[x+dx[i]][y+dy[i]]==0:
            a[x][y] = 1
            c+=1
            dfs(a,x+dx[i],y+dy[i])
            c-=1#回退到这个格子
    a[x][y]=0
            #走完要重置！回退到上个格子 走到下一步之前再记录
dfs(a,1,1)
if w:
    print("Yes")
else:
    print("No")




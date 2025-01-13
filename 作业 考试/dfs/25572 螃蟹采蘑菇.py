
c='no'
def valid(x,y):
    if 0<=x<n and 0<=y<n and a[x][y]!=1 and visited[x][y]==0:
        return True
    return False
#直接用两个格情况比较复杂，记录不走回头路会WA！
#用一个点作指针
def dfs(x1,y1):
    global c
    if Type==1:
        x2=x1+1
        y2=y1
    else:
        x2=x1
        y2=y1+1
    #print(x1,y1,x2,y2)
    if a[x1][y1]==9 or a[x2][y2]==9:
        c='yes'
        return
    for dx,dy in dir:
        nx1=x1+dx
        nx2=x2+dx
        ny1=y1+dy
        ny2=y2+dy
        if valid(nx1,ny1)and valid(nx2,ny2) and (nx1,ny1)not in visited:
            visited[x1][y1]=1
            dfs(nx1,ny1)
            visited[x1][y1] = 0
    return

n=int(input())
visited=[[0]*n for i in range(n)]
a=[list(map(int,input().split())) for i in range(n)]
dir=[(0,1),(0,-1),(1,0),(-1,0)]
for i in range(n):
    for j in range(n):
        if a[i][j]==5:
            x01=i
            y01=j
            if i<n-1:
                if a[i+1][j]==5:
                    Type=1
            if j<n-1:
                if a[i][j+1]==5:
                    Type=2
            #只执行一次!
            dfs(x01,y01)
            print(c)
            exit()#退出所有循环 break只一层！

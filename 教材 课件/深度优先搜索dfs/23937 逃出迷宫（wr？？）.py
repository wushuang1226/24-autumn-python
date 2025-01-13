#如果可以返回的话 辅助visited[]记录已访问过的跳过
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]

dir=[(0,1),(1,0)]
def dfs(x,y):
    #print(x,y)
    if x==n-1 and y==n-1:
        return "Yes"
    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        if nx<n and ny<n and a[nx][ny]==0:
            return dfs(nx,ny)
    return"No"

if a[0][0]==1:######%$#%^&*
    print("No")
else:
    print(dfs(0,0))


#这个做过呜呜但是忘干净了。
#dp的特点：每个格子有对应的数值，且要规划恰当的顺序遍历
r,c=map(int,input().split())
a=[[10001]+list(map(int,input().split())) +[10001] for i in range(r)]
a.append([10001]*(c+2))
a.insert(0,[10001]*(c+2))
dp=[[1]*(c+2) for i in range(r+2)]
dir=[(1,0),(-1,0),(0,1),(0,-1)]

b=[]
for i in range(1,r+1):
    for j in range(1,c+1):
        b.append([a[i][j],i,j])
b.sort()
#从低到高，前面的不会对后面造成影响！
for height,x,y in b:
    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        if a[nx][ny]<height:
            dp[x][y]=max(dp[x][y],dp[nx][ny]+1)

c=[]
for i in dp:
    c.append(max(i))
print(max(c))




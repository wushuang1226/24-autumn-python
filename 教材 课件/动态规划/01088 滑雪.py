r,c=map(int,input().split())
#rc别搞反。。用不等调试
a=[]
b=[]
circle=[[-1,0],[0,-1],[0,1],[1,0]]#dx\dy
dp=[[0]*(c+2)]+[[1]*(c) for i in range(r)]+[[0]*(c+2)]
for i in range(1,r+1):
    dp[i]=[0]+dp[i]+[0]#需要扩容的其实是a。。
for i in range(r):
    a.append(list(map(int,input().split())))
#书里很棒的优化，将所有点按高度大小排序！再从小到大算每个点
for i in range(r):
    for j in range(c):
        b.append([a[i][j],i+1,j+1])
        #加保护圈要加一！

a=[[0]*(c+2)]+a+[[0]*(c+2)]
for i in range(1,r+1):
    a[i]=[0]+a[i]+[0]
b.sort()
for k in b:
    for i in circle:
        if a[k[1]][k[2]] > a[k[1] + i[0]][k[2] + i[1]]:
            dp[k[1]][k[2]]=max(dp[k[1]+i[0]][k[2]+i[1]]+1,dp[k[1]][k[2]])
print(max(max(i) for i in dp))#不一定最大那个路径最长！
'''
r, c = map(int, input().split())
node = []       # height of each element
node.append( [100001 for _ in range(c+2)] )
for _ in range(r):
    node.append([100001] +[int(_) for _ in input().split()] + [100001])
node.append( [100001 for _ in range(c+2)] )
更简洁的保护圈
dp = [[0]*(c+2) for _ in range(r+2)]
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

def dfs(i,j):
    if dp[i][j]>0:
        return dp[i][j]
    思路为dfs，且避免重复计算
    for k in range(4):       
        if node[i+dx[k]][j+dy[k]] < node[i][j]:
            dp[i][j] = max( dp[i][j], dfs(i+dx[k], j+dy[k])+1 )

    return dp[i][j]

ans = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        ans = max( ans, dfs(i,j) )
#初始加一
print(ans+1)'''
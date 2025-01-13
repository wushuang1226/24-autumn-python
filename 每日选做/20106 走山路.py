#dijkstra bfs 最短距离问题，用优先队列代替普通的顺序
import heapq
dir=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y):
    q=[]
    sweat=[[float('inf')] * n for _ in range(m)]
    sweat[x][y]=0#列表而非集合记录走过的值
    heapq.heappush(q,(0,x,y))
    while q:
        s,x,y=heapq.heappop(q)#s小的优先弹出
        if x==ei and y==ej:
            return s
        for dx,dy in dir:
            nx=x+dx
            ny=y+dy
            if 0<=nx<m and 0<=ny<n and a[nx][ny]!="#":
                if sweat[nx][ny]>s+abs(int(a[nx][ny])-int(a[x][y])):
                    sweat[nx][ny] = s + abs(int(a[nx][ny]) - int(a[x][y]))
                    heapq.heappush(q,(sweat[nx][ny],nx,ny))
                #不回头？不是的，如果有更优解可以
    return "NO"
m,n,p=map(int,input().split())
a=[input().split() for i in range(m)]
for _ in range(p):
    si,sj,ei,ej=map(int,input().split())
    if a[si][sj]=="#" or a[ei][ej]=="#":
        print("NO")
    else:
        print(bfs(si,sj))
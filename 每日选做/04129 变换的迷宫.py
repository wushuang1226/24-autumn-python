#细节超级超级重要呜呜呜呜呜
t=int(input())
for _ in range(t):
    r,c,k=map(int,input().split())
    a=[list(input()) for i in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j]=='S':
                sx=i
                sy=j
                break

    from collections import  deque
    dir=[(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(x,y):
        global k
        q=deque()
        inq=set()
        q.append((x,y,1))
        inq.add((x,y,1))#默认不走回头路？No!可以回头，只是要排除绕圈
        while q:
            x,y,time=q.popleft()
            __=time%k
            for (dx,dy) in dir:
                nx=x+dx
                ny=y+dy#zaibuxiaoxinqiaocuo woyaodanile!
                #print(nx,ny)
                if 0<=nx<r and 0<=ny<c and (nx,ny,__) not in inq:
                    if a[nx][ny]=="E":
                        return time
                    elif a[nx][ny]!='#' or __==0 :#可能回起点。
                        q.append((nx,ny,time+1))
                        inq.add((nx,ny,__))
        return "Oop!"

    print(bfs(sx,sy))
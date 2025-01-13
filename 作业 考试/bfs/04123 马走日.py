#保护圈or辅助列表n 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]

#法一 dfs递归
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,-2,2,-2,2,-1,1]
c=0
def dfs(ok,x,y):
    global c#列表默认全局
    if ok==n*m:
        c+=1
        return
    for i in range(8):
        if a[x+dx[i]][y+dy[i]]==0:
            #if chess[s][t]==False and 0<=s<n and 0<=t<m :
            a[x + dx[i]][y + dy[i]] = 1
            dfs(ok+1,x+dx[i],y+dy[i])
            a[x + dx[i]][y + dy[i]] = 0
            #“回溯”
            #走完要重置！走到下一步之前再记录

t=int(input())
for i in range(t):
    n,m,x0,y0=map(int,input().split())
    a=[[1]*(m+4),[1]*(m+4)]
    for j in range(n):
        a0=[1,1]+[0]*m+[1,1]
        a.append(a0)
    a[x0+2][y0+2]=1
    a.append([1]*(m+4))
    a.append([1]*(m+4))

    dfs(1,x0+2,y0+2)
    print(c)
    c=0#...。。别犯这种错误

#法二 bfs
'''for case in test_cases:
        n, m, start_x, start_y = case
        total_squares = n * m

        # 初始化栈
        stack = [(start_x, start_y, [(start_x, start_y)])]
        paths_count = 0

        while stack:
            x, y, path = stack.pop()

            if len(path) == total_squares:
                paths_count += 1
                continue

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in path:
                    stack.append((nx, ny, path + [(nx, ny)]))

        results.append(paths_count)'''


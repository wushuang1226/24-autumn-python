#还是在抄答案，但是要学！
from collections import deque
n,m=map(int,input().split())
a=x=[[-1]*(m+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(n)]+[[-1]*(m+2)]
inq = set()
dx=[-1,0,0,1]
dy=[0,-1,1,0]

def  bfs(x,y):#不再涉及调用自身的递归
    q=deque([(x,y)])
    inq.add((x,y))
    #!!!!!程序化结构
    while q:#把这一步添加的元素过完
        front=q.popleft()#从最先进去的开始，逐个遍历
        for _ in range(4):
            nx=front[0]+dx[_]
            ny=front[1]+dy[_]
            if  a[nx][ny]==1 and (nx,ny) not in inq:
                inq.add((nx,ny))
                q.append((nx,ny))

c=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]==1 and (i,j) not in inq:
            bfs(i,j)
            c+=1
print(c)


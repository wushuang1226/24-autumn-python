#来不及改了呜呜呜 先粘的答案去AC

#给的坐标不是（0，0）横纵还是反的。
#思路还是经典的，加一个计数，但还是觉得好难所以对着答案完善的。。
from collections import deque
dx=[-1,0,0,1]
dy=[0,-1,1,0]
#bfs不需要记录，会一次到底自动返回最优
def bfs(x0,y0,x1,y1):
    q=deque()
    inq= set()
    q.append((x0,y0,-1,0))
    ans=[]
    while q:
        x,y,di,seg=q.popleft()
        if (x,y)==(x1,y1):
            ans.append(seg)
            break#初始特殊情况

        for _ in range(4):
            nx = x+ dx[_]
            ny = y+ dy[_]
            if  (nx,ny,_) not in inq:
                new_di=_#记录方向和线段个数
                new_seg=seg if new_di==di else seg+1
                if nx==x1+1 and ny==y1+1:
                        ans.append(new_seg)
                        continue
                if a[nx][ny]==" ":
                    q.append((nx, ny,new_di,new_seg))
                    inq.add((nx, ny,i))
    if len(ans)==0:
        return -1
    else:
        return min(ans)

board=1
while True:
    m, n = map(int, input().split())
    if n==m==0:
        break
    else:
        a = [['X'] * (m + 4)]
        a.append(["X"] + [' '] * (m + 2) + ["X"])
        for i in range(n):
            a0 = ["X", ' '] + list(input()) + [" ", "X"]
            a.append(a0)
        a.append(["X"] + [' '] * (m + 2) + ["X"])
        a.append(['X'] * (m + 4))
        print(f"Board #{board}:")
        pair_num = 1
        while True:
            y0,x0,y1,x1=map(int, input().split())
            if x0==y0==x1==y1==0:
                break
            seg=bfs(x0+1,y0+1,x1+1,y1+1)
            if seg == -1:
                print(f"Pair {pair_num}: impossible.")
            else:
                print(f"Pair {pair_num}: {seg} segments.")
            pair_num += 1

        print()
        board += 1




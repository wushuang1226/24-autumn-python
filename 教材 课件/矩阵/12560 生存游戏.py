
'''保护圈：
dx = [-1, -1, -1, 0, 1, 1,  1,  0]
dy = [-1,  0,  1, 1, 1, 0, -1, -1]
也可以不加保护圈用min max
row_s, row_e = max(0, i-r), min(n-1, i+r)
    col_s, col_e = max(0, j-r), min(m-1, j+r)
——总之要利用一个函数生成新表
def check(board, y, x):
    c = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        c += board[ny][nx]

    if board[y][x] and (c<2 or c>3):
        return 0
    elif board[y][x]==0 and c==3:
        return 1
更快的补齐边的方式
for _ in range(n):
    board.append([0] +[int(_) for _ in input().split()] + [0])
最后的输出创造一个新的空列表，也可避免浅拷贝问题'''
n,m=map(int,input().split())
a=[list(map(int,input().split()))for i in range(n)]
import copy
a0=copy.deepcopy(a)
for i in a0:
    i.insert(0, 0)
    i.append(0)
a0.insert(0,[0]*(m+2))
a0.append([0]*(m+2))
#边缘只是不是8个 也要看。
#深拷贝不可更改
for i in range(1,n+1):
    for j in range(1,m+1):
        b=[a0[x][y] for x in range(i-1,i+2) for y in range(j-1,j+2)]
        b=sum(b)-a0[i][j]
#这里的b是一个一维列表 加[]为二维
        if a0[i][j]==1:
            #避免逻辑词运算错误
            if b==2 or b==3:
                continue
            else:
                a[i-1][j-1]=0
        else:
            if b==3:
                a[i-1][j-1]=1
for i in a:
    print(*i)
#emmmm一定好好理解提示。。其实不需要绕这么大一个圈子，只需要枚举第一行按什么灯即可
a=[[0]+list(map(int,input().split())) +[0]for i in range(5)]
a.append([0]*8)
a.insert(0,[0]*8)

from copy import deepcopy#深拷贝列表
#调换rmap={0:1,1:0}
def turn(_):
    if _==1:
        return 0
    else:
        return 1

def black(x):
    y=[[0]*8 for i in range(7)]
    for i in range(5):
        for j in range(1,7):
            #print(i,j)
            if x[i][j]==1:
                y[i+1][j]=1
                x[i][j]=turn(x[i][j])
                x[i+1][j]=turn(x[i+1][j])
                x[i+1][j+1]=turn(x[i+1][j+1])
                x[i+1][j-1]=turn(x[i+1][j-1])
                x[i+2][j]=turn(x[i+2][j])
    return y

from itertools import product#数对生成器
for test in product(range(2), repeat=6):
    a1=deepcopy(a)
    a1[0][1:7]=list(test)
#多重循环嵌套很容易出各种各样的问题。。
    b1=black(a1)
    if sum(a1[5][1:7]) == 0:
        for j in range(1, 6):
            print(*b1[j][1:7])

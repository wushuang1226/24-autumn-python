#数量级只有1000，大胆写先
#不可悬空！关注三个点
import math
while True:
    R,n=map(int,input().split())
    if R==n==-1:
        break
    else:
        a=list(map(int,input().split()))
        a.sort()
#统一列表建立窗口
#其实直接加减R也完全OK
        b=[[i-R,i,i+R] for i in a]
        left=0
        center=0
        i=0
        c=0
        #开头比较特殊 不一定从第一个开始
        while i<n:
            while i<n and b[left][2]>=b[i][1]:#避免超出范围
                i+=1
            center=i-1
            c+=1
            #while比for好用 i可随时修改
            while i<n and b[center][2]>=b[i][1]:
                i+=1
            left=i

        print(c)




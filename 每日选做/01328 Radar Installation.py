#对象反转 转换为一维轴线上的贪心问题
#这题看教材的时候学过思路 之前那个进程检测也做过类似的啦
import math
case=1
while True:
    n,d=map(int,input().split())
    if n==d==0:
        break
    else:
        a=[]
        a0=[]
        c=0
        for i in range(n):
            x,y=map(int,input().split())
            a0.append([x,y])
            if y>d:
                c=-1
        if c==-1:
            print(f"Case {case}: -1")
        else:
            for i in range(n):
                z = math.sqrt(d ** 2 - a0[i][1] ** 2)
                a.append([a0[i][0] - z, a0[i][0] + z])
            a.sort(key=lambda x:x[1])
            k=a[0][1]
            b=1
            for i in range(1,n):
                if a[i][0]<=k:
                    continue
                else:
                    k=a[i][1]
                    b+=1
            print(f"Case {case}: {b}")
        input()
        case+=1

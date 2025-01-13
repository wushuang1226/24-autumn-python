##区间覆盖贪心题目(应该还挺经典）##嗯呢 非常经典
#教材上类似的雷达：反向思维——将雷达覆盖的船转换为船能接收到信号的雷达坐标范围
k=int(input())
for i in range(k):
    n=int(input())
    a=[]
    t=1
    x=0
    for i in range(n):
        a.append(list(map(int,input().split())))
    #a.sort()不可以
    #要用截止时间排序，否则[1,5][2,4]会出问题
    a.sort(key=lambda x:x[1])
    for i in range(n):
        if a[x][1]<a[i][0]:
            x=i
            t+=1
    print(t)
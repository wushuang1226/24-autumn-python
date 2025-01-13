while True:
    n,m=map(int,input().split())
    a=[i+1 for i in range(n)]
    b=0
    k=n
    if n+m==0:
        break
    while len(a)>1:
        if b+m<=k:
            b+=m
            a.remove(a[b-1])
            k-=1
            b-=1
        else:
            while b+m>k:
                b-=k
            b+=m
            a.remove(a[b-1])
            k-=1
            b-=1
    for i in a:
        if i!=0:
            print(i)
'''
while len(monkeys) > 1:
# 计算当前出圈的猴⼦的位置
pos = (pos + m - 1) % len(monkeys)#取模超好用！！！
# 移除出圈的猴⼦
monkeys.pop(pos)
return monkeys[0] # 返回最后剩下的猴⼦的编号'''


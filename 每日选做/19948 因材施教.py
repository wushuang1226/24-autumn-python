#务必务必用完测试数据
#极差减去两个相邻最大差 类似差减法
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

b=[a[i+1]-a[i] for i in range(n-1)]
b.sort()
#sort非常快！
'''for i in range(m-1):#m个班两个空。
    c.append(max(b))
    b.remove(max(b))'''

print(a[-1]-a[0]-sum(b[n-m:]))


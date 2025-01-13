n,w=map(int,input().split())
a=[]
weight=0
value=0
"""更巧妙的方法：p/q代表了单位重量的价值
value = sum(candies[:w])
"""
for i in range(n):
    p,q=map(int,input().split())
    a.append([p,q,p/q])
def f(x):
    return x[2]
a.sort(reverse=True,key=f)
"""可以拆成散装！要看平均值。。"""
for i in a:
    if weight+i[1]<=w:
        weight+=i[1]
        value+=i[0]
    else:
        value+=((w-weight)/i[1])*i[0]
        break

print('%.1f'%(value))



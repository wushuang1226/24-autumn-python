n=int(input())
a=[]
def f(x):
    return x[0]
def l(x):
    return x[1]
for i in range(n):
    a.append(list(map(int,input().split())))

a.sort(key=f)
b=tuple(a)
a.sort(key=l)
c=tuple(a)
#用元组锁定列表sort顺序
if b==c:
    print( "Poor Alex")
else:
    print( "Happy Alex")

t=int(input())
for i in range(t):
    n=int(input())
    b=1
    c= {1}
    while b<=n:
        c.add(b)
        b=b*2
    '''枚举会超时 直接用公式！！！！！
    上面还可以
    x=int(math.log2(n))再循环
    下面不可以for i in range(1,n+1):#左开右闭！！！！！
        if i in c:
            a-=i
        else:
            a+=i'''
    a=(1+n)*n/2-2*sum(c)
    print(int(a))

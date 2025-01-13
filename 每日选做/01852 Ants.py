##不要被骗啦。。。。两只相遇后反向其实也还是在往前走嘛。。
#方向讨论2**n过大，所以可能就不需要讨论。
#看每只离端点的距离即可

t=int(input())
for _ in range(t):
    l,n=map(int,input().split())
    a=list(map(int,input().split()))
    mi=0
    ma=0
    for i in range(n):
        mi=max(mi,min(l-a[i],a[i]))
        ma=max(ma,max(l-a[i],a[i]))
    print(mi,ma)


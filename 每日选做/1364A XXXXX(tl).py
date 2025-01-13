t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(lambda y:int(y)%x,input().split()))
    k=-1
    d=n-1
    c=0
    while d>=0 and c==0:
        for i in range(n-d):
            if sum(a[i:i+d+1])%x!=0:
                k=d+1
                c=1
                break
        d-=1
    print(k)
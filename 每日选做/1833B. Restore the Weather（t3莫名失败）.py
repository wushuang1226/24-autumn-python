#呜呜呜呜不会做了
t=int(input())

for _ in range(t):
    n=list(map(int,input().split()))[0]
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=tuple(a)
    a.sort()
    b.sort()
    f=[a for a in range(n)]
    g=list(c)
    for i in range(n):
        if len(a)==0:
            break
        for j in range(n-i):
            if g[i]==a[j]:
                f[i]=b[j]
                a.remove(a[j])
                b.remove(b[j])
                break
    for i in f:
        print(i,end=" ")
    print()
                
            

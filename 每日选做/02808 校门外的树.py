a=list(map(int,input().split()))
l=a[0]
m=a[1]
#l,m=!!!不用建列表
b=[1 for i in range(l+1)]#[1]*()
for i in range(m):
    c=list(map(int,input().split()))
    #s,t=map...
    for j in range(c[0],c[1]+1):
        #+1很重要哦~
        b[j]=0
print(sum(b))

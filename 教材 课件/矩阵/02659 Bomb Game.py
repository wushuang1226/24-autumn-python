#+1-1!!!!!!!!
a,b,k=map(int,input().split())
l=[[1]*b for i in range(a)]
def change(l,r,s,d,t):
    up,down=max(r-d,0),min(r+d,a-1)
    left,right=max(s-d,0),min(s+d,b-1)
    if t==1:
        for i in range(a):
            for j in range(b):
                 if not (up<=i<=down and  left<=j<=right ):
                    l[i][j]=0
    else:
        for i in range(up,down+1):
            for j in range(left,right+1):
                l[i][j]=0
                #用最简单的逻辑 哪怕麻烦一点
    return l

for i in range(k):
    r,s,p,t=map(int,input().split())
    l=change(l,r-1,s-1,p//2,t)
l0=[j for i in l for j in i]
print(sum(l0))

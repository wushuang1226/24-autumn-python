n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
y=0
for i in a:#hang
    for j in range(m):#lie
        A=a[0][j]
        C=a[n-1][j]
        D=i[0]
        B=i[m-1]
        z=int(str(A)+str(B)+str(C)+str(D))
        z0=i[j]*int(z)
        y=max(y,z0)
print(y)
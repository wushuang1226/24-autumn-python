m,n,p,q=map(int,input().split())
#a=b=[]不能这么写 会串台
a=[]
b=[]
k=[]
#C = [[0 for x in range(n+1-q)] for i in range(m+1-p)]   #二维矩阵上的卷积运算
#答案也可以直接构建一个矩阵
for i in range(m):
    a.append(list(map(int,input().split())))
for i in range(p):
    b.append(list(map(int,input().split())))
for y in range(m+1-p):
    d=[]
    for x in range(n+1-q):
        c=0
        for i in range(p):
            for j in range(q):
                c+=a[y+i][x+j]*b[i][j]
        d.append(str(c))
    k.append(" ".join(d))
print('\n'.join(k))






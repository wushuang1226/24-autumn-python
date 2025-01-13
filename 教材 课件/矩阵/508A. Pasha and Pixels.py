n,m,k=map(int,input().split())
#a=[[0]*(m+2)]*(n+2)不可以浅拷贝！！
a=[[0]*(m+2)for i in range(n+2)]
#每次只需要查周围四个
dx=[0,1,1,0]
dy=[0,1,0,1]
def check(a,i,j):
    c=0
    b=[]
    for y in range(4):
            b.append(a[i+dx[y]][j+dy[y]])
            c+=a[i+dx[y]][j+dy[y]]
    if c==4:
            return 1
    c = 0
    i+=1
    for y in range(4):
        c += a[i + dx[y]][j + dy[y]]
    if c == 4:
        return 1
    c=0
    j += 1
    for y in range(4):
        c += a[i + dx[y]][j + dy[y]]
    if c == 4:
        return 1
    c=0
    i -= 1
    for y in range(4):
        c += a[i + dx[y]][j + dy[y]]
    if c == 4:
        return 1

for z in range(k):
    i,j=map(int,input().split())
    #输入大了1！
    a[i][j]=1
    if check(a,i-1,j-1):
        print(z+1)
        break
else:
    print(0)

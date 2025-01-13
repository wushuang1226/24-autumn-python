#模拟
n=int(input())
#浅拷贝会联动！！a=[[1]*(n+2)]+[[1]+[0]*n+[1]]*n+[[1]*(n+2)]
a=[[1]*(n+2)]
for i in range(n):
    a.append([1]+[0 for j in range(n)]+[1])
a.append([1]*(n+2))
b=[[0,1],[1,0],[0,-1],[-1,0]]#很好啦
direction=0
c=1
x=1
y=1
while True:
    if c==n**2+1:
        for i in range(1,n+1):
            print(*a[i][1:n+1])
        break
    a[x][y]=c
    if a[x+b[direction][0]][y + b[direction][1]]!=0:
        direction+=1
        if direction==4:
            direction=0
    x=x+b[direction][0]
    y = y + b[direction][1]
    c+=1

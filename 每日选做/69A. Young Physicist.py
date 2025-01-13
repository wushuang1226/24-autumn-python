#矩阵
n=int(input())
x,y,z=[],[],[]
for i in range(n):
    a=list(map(int,input().split()))
    x.append(a[0])
    y.append(a[1])
    z.append(a[2])
if sum(x)==sum(y)==sum(z)==0:
    print("YES")
else:
    print("NO")
#x=0;x+=a[0]
#sum=[0]*3;sum=list(map(lambda x,y:x+y,s,sum)
#两个列表同列叠加

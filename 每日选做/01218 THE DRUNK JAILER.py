#数学思维：只有完全平方数有奇数个因数！！
n=int(input())
def change(x):
    if x==0:
        return 1
    if x==1:
        return 0
for i in range(n):
    m=int(input())
    a=[0]*(m+1)
    for j in range(1,m+1):
        #for k in range(j,m+1,j)步长
        for k in range(1,m+1):
            if k%j==0:
                a[k]=change(a[k])
    print(sum(a))

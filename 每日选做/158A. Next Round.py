#把用空格分割的数字转化为整数列表
a=list(map(int,input().split()))
b=list(map(int,input().split()))
#或者b=[int(x) for x in input().split()]
k=a[1]
line=b[k-1]
#计数器 循环
c=0
for x in b:
    if x<=0:
        break
    elif x>=line:
        c=c+1
    else:
        break
print(c)

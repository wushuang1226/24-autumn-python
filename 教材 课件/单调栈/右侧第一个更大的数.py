a=list(map(int,input().split()))
n=len(a)
b=[-1]*n
stack=[]#堆里是序号
for i in range(n):
    while stack and a[i]>a[stack[-1]]:#非空递减栈
#while循环！弹出所有不符合条件的直到可以继续
        top=stack.pop()
        b[top]=a[i]
    stack.append(i)
print(b)
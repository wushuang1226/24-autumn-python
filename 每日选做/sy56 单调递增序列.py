#定义函数
n=int(input())
b=list(map(int,input().split()))
c=0
for i in range(n-1):
    if b[i]>b[i+1]:
        print("NO")
        c=1
        break
if c==0:
    print("YES")
    

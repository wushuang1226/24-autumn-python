n=int(input())
a=[[int(i) for i in input().split() ]for j in range(n)]
ans=[]
for _ in range(n//2):
    num=sum(a[0]+a[-1])
    a=a[1:-1]
    for i in range(len(a)):
        num+=a[i][0]+a[i][-1]
        a[i]=a[i][1:-1]
    ans.append(num)
if len(a)!=0:#首尾特殊
    ans.append(a[0][0])
print(max(ans))
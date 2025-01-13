#二分查找
n,c=map(int,input().split())
a=[int(input()) for i in range(n)]
a.sort()
def check(mid,c):
    num=1
    point=a[0]
    for i in range(1,n):
        if a[i]-point>=mid:
            num+=1
            point=a[i]#顺序别反。。。
    if num>=c:
        return True
    else:
        return False

left=0
right=(a[-1]-a[0])//c+1
ans=-1
while left<=right:
    mid=(left+right)//2
    #print(left,mid,right)
    if check(mid,c):
        ans=mid
        left=mid+1
    else:
        right=mid-1
print(ans)


##二分查找
l,n,m=map(int,input().split())
a=[int(input()) for i in range(n)]
a.append(l)

def check(mid):
    point = 0
    c = 0
    for i in range(n+1):
        if a[i] - point < mid:
            c += 1
        else:
            point = a[i]
    if c<=m:
        return True
    else:
        return False
left=0
right=l
ans=-1
while left<=right:
    mid=(left+right)//2
    #print(mid,c)
    if check(mid):
        #可行上界 可能更大
        ans=mid
        left=mid+1
    else:
        right=mid-1
        #不可行下界
print(ans)

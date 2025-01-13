a=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
t=3
n=len(a)
m=len(a[0])
b=[j for i in a for j in i]

ans='false'
l=0
r=n*m-1
while l<=r:
    mid=(l+r)//2
    if b[mid]<t:
        l=mid+1
    elif b[mid]>t:
        r=mid-1
    else:
        ans='true'
        break
print(ans)



n,l=map(int,input().split())
a=list(map(int,input().split()))
if n==1:
    print(max(a[0],l-a[n-1]))
else:
    a.sort()
    b=[a[i+1]-a[i] for i in range(n-1)]
    print(max(max(b)/2,a[0],l-a[n-1]))
#max两两比较省空间？但时间会慢    ans = max(ans, (a[i+1]-a[i])/2)

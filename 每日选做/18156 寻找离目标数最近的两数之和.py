#题目中给到的信息务必务必用全
import bisect
t=int(input())
s=list(map(int,input().split()))
s.sort()
l=0
r=len(s)-1#-1!
#开头要考虑特殊情况，但通常不要分开写
a=[]
while l<r:
    a.append(s[l]+s[r])
    if s[l] + s[r] < t:
        l += 1
    elif s[l] + s[r] > t:
        r -= 1
    else:
        break
a.sort()
point=bisect.bisect_left(a,t)#二分查找的序号有序性！
if point==len(a):
    print(a[-1])
elif point==0:
    print(a[0])
else:
    b1=a[point]-t
    b2=t-a[point-1]
    if b2<=b1:
        print(a[point-1])
    else:
        print(a[point])

'''更简洁的方法：即时更新答案，记录最小绝对值
if mid == tar:
        ans = mid
        break
    
    if abs(mid - tar) < gap:
        gap = abs(mid - tar)
        ans = mid
    if abs(mid - tar) == gap:
        ans = min(ans, mid)'''
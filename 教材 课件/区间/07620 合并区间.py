#左端点排序，右端指针
#力扣过了，OJ WA不管了。。。
n=int(input())
intervals=[]
for i in range(n):
    intervals.append(list(map(int,input().split())))
intervals.sort()
a=[]
l=intervals[0][0]
r=intervals[0][1]
n=len(intervals)-1
for i in range(1,len(intervals)):
            if intervals[i][1]<=r:#一定用指针作比较对象，不要用i-1
                continue#嵌套，可能多个！
            elif intervals[i][0]<=r:
                r=intervals[i][1]
            else:
                a.append([l,r])
                l=intervals[i][0]
                r=intervals[i][1]
a.append([l,r])
for i in a:
    print(*i)
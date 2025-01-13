#特别典型的贪心应用基础！！用区间右端来排序！！
#（通常会转化成区间选点最少问题）
#洛谷的代码 在调试
n=int(input())
intervals=[]
for i in range(n):
    intervals.append(list(map(int,input().split())))
for i in range(1):
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        a=[]
        n=len(intervals)
        c=0
        r=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]<r:
                c+=1
            else:
                r=intervals[i][1]
                a.append(intervals[i])
        print(a)
        """intervals.sort(key=lambda x: (x[0], x[1]))
        print(intervals)
        a = []
        n = len(intervals)
        c = 0
        r = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] < r:
                c += 1
            else:
                r = intervals[i][1]
                a.append(intervals[i])
        print(a)"""


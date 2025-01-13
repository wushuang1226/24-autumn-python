#最长时间：最慢的快递 或者自己
t=int(input())
ans=[]
for _ in range(t):
    m=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    #排序还是没选对。c.sort(key=lambda x:(x[0],-x[1]))
    c = sorted(list(zip(a, b)), reverse=True)
    d = 0
    for i in range(m):
        d += c[i][1]
        if d >= c[i][0]:
            d = max(c[i][0], d - c[i][1])
            #派送时间越来越小，前缀和越来越大，两个都单调，类似于双指针查找
            break

    ans.append(d)

print('\n'.join(map(str, ans)))#大数据量，ans列表储存，一起输出








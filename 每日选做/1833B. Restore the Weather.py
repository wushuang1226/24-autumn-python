t = int(input())
for _ in range(t):
    j, k = map(int, input().split())

    l1 = list(map(int, input().split()))
    v = [(l1[i], i) for i in range(j)]
    #用嵌套赋予原始顺序坐标
    v.sort()

    l2 = list(map(int, input().split()))
    l2.sort()

    z = [0] * j
    for i in range(j):
        z[v[i][1]] = l2[i]
        #思路是对的，相同大小位置的匹配在一起，并利用坐标进行定位

    for data in z:
        print(data, end=" ")
    print()
    #最后的空行记得哦~

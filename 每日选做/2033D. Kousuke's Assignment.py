#贪心——求和问题前缀和思想！
#贪心的简化：从左往右扫当前扫到的位置可以作为“美丽的”子段的最右端时一定将它作为一个子段
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix_sum = 0
    prefix_sums = set()
    count = 0

    for num in a:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in prefix_sums:#和相等说明有一段为零
            count += 1
            prefix_sum = 0
            prefix_sums.clear()
            #即时分割出子段并清空前缀和记录
        else:
            prefix_sums.add(prefix_sum)
    print(count)

    #如果用dp会超时
    '''suma = 0
    prefix = {0: -1}#把集合换成了字典
    ans = 0
    mark = -1
    for i in range(n):
        suma += a[i]
        if suma in prefix and prefix[suma] >= mark:
            ans += 1
            mark = i#并记录上一个子段的结尾
        prefix[suma] = i#每一个子段的起始'''
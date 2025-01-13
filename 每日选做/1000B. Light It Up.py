'''分析：加一次操作相当于
1.把某个区间拆成两个，肯定为一开一关，让开最大（即该数字-1）
2.操作之后的开灯时长为：该数字之前的总开灯时长+该数字之后的总关灯时长+本区间改变之后的开灯时长(区间长度-1）

# 如本区间长度大于1且为开灯状态，操作后开灯时长为：b[i] -1 + m-a[i]-(b[n+1]-b[i])
# 如本区间长度大于1且为关灯状态，操作后开灯时长为：b[i] + a[i]-a[i-1]-1 + m-a[i]-(b[n+1]-b[i])
# 所以遍历一遍维护最大值即可。另外可以不操作，此时开灯时长为b[n+1]。'''


f = 1  # switch
n, M = map(int, input().split())
a = [0] + [int(x) for x in input().split()] + [M]
b = [0] * (n + 2)
# 记录到第i次操作时亮灯时长，记为b[i].
for i in range(1, n + 2):
    b[i] = b[i - 1] + f * (a[i] - a[i - 1])
    f ^= 1  # 0->1 or 1->0

ans = b[n + 1]  # untouched
for i in range(1, n + 2):
    if (a[i] - a[i - 1] > 1):
        if i & 1:#奇数
            # ans = max(ans, b[i]+M-a[i]-(b[n+1]-b[i])-1)小于偶数
            pass
        else:
            ans = max(ans, b[i] + a[i] - a[i - 1] - 1 + M - a[i] - (b[n + 1] - b[i]))

print(ans)
#双dp，一个用作辅助！
#第k个作结尾的dp 是对的
a = list(map(int, input().split(',')))
dp1 = [0] * len(a)#不放回的基准dp
dp2 = [0] * len(a)#可放回一个，如果更优的话
dp1[0] = a[0]
dp2[0] = a[0]
for i in range(1, len(a)):
    dp1[i]=max(dp1[i-1]+a[i],a[i])#连续or新起
    dp2[i]=max(dp1[i-1],dp2[i-1]+a[i],a[i])#不取第2个，或保留不取前面某一个，或都取到
print(dp1,dp2)
print(max(dp2))
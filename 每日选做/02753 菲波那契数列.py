n=int(input())
for i in range(n):
    a=int(input())
    if a==1:
        print(1)
    elif a==2:
        print(1)
    else:
        b=[1,1]
        for i in range(a-2):
            b.append(b[-1]+b[-2])
        print(b[-1])
'''
更严格的数学定义
def f(n):
    if n <= 2:
        return 1
    else:
        return f(n-1)+f(n-2)
省去重复的无效计算
用一个列表存储记忆并反复调用
def f(n):
    if n <= 2:
        return 1
    if 10.27-11.1 dp[n] != -1:
        return 10.27-11.1 dp[n]
    else:
        10.27-11.1 dp[n] = f(n-1)+f(n-2)
        return 10.27-11.1 dp[n]
10.27-11.1 dp = [-1]*21
放在一个列表里能节省时间
ans.append(f(num))
print('\n'.join(map(str, ans)))
'''''
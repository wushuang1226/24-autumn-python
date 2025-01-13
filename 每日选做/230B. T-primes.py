#建立素数表的方法!!
#法一 埃氏筛（略）
#法二 欧拉筛
#其实可以不要primes列表
def all_primes(n):
    is_prime=[True]*(n+1)#初始化全是素数
    is_prime[1]=False#!!!1不是质数
    primes=[]
    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i*p>n:
                break
            is_prime[i*p]=False
            if i%p==0:
##确保每个合数只被其最小素因子标记一次
                break
    return is_prime

s = all_primes(1000000)

input()
for i in map(int, input().split()):
    sqrt_i = i ** 0.5#奇数素数为完全平方
    if sqrt_i % 1 == 0:  # 对于浮点数，x % 1 == 0 用于检查 x 是否是一个整数。
        if s[int(sqrt_i)]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

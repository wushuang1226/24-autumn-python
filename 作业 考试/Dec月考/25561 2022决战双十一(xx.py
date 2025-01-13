#遍历 dfs 数量级在个位
n,m=map(int,input().split())
price=[]
coupon0=[]
num=0
cou=[[] for i in range(m)]
for i in range(n):
    price.append([int(j[2:]) for j in input().split()])
for i in range(m):
    coupon0.append(list(input().split()))
for j in range(m):
    for _ in coupon0[j]:
        cou[j].append(list(map(int,_.split('-'))))
print(price,cou)


print(num-(num//300)*50)
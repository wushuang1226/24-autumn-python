###0-1背包 选或不选，倒序
#如果重量可以随意分割，就是之前的找平均最大
#昨天看了答案
#每个物品可取可不取，求前i个物品j重量内最大价值
n,b=map(int,input().split())
p=[0]+list(map(int,input().split()))
w=[0]+list(map(int,input().split()))
value=[[0]*(b+1) for i in range(n+1)]
#多设一列
for i in range(1,n+1):
    for j in range(1,b+1):
        if w[i]<=j:
            value[i][j]=max(value[i-1][j-w[i]]+p[i],value[i][j])
        else:
            value[i][j]=value[i-1][j]
print(value)
print(value[-1][-1])

#滚动数组
value2=[0]*(b+1)
for i in range(1,n+1):
    for j in range(b,w[i]-1,-1):#注意倒序
        value2[j]=max(value2[j-w[i]]+p[i],value2[j])
print(value2)
print(value2[-1])


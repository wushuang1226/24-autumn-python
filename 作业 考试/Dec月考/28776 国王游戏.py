#从特殊情况入手 eg最后一个
#控制变量分析：对于每个人而言，越往后站获利越大，所以考虑最后一个人即可
#而计算最后一个人的金币，所有人左手总乘积是个定值
#可以猜猜？按乘积排序
n=int(input())
c0=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append(list(map(int,input().split())))
c.sort(key=lambda x:x[0]*x[1])
left=c0[0]
ans=[]
for i in range(n):
    left*=c[i][0]
    ans.append(left//(c[i][0]*c[i][1]))
print(max(ans))


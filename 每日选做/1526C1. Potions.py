#法一 后悔贪心，不符合了再处理
import heapq
n=int(input())
a=list(map(int,input().split()))
health=0
consumed=[]#已经喝下去的
for i in a:
    health+=i
    heapq.heappush(consumed,i)
    if health<0:
        if consumed:#非空
            health-=consumed[0]#复原
            heapq.heappop(consumed)#去除已有最小的
#print(consumed)
print(len(consumed))

#法二 喝下数量为j瓶药水后 剩余最大生命值dp
'''# 李佳聪 24工学院
a=int(input())
potions=list(map(int,input().split()))
dp=[-float('inf')]*(1+a)
dp[0]=0
for i in range(1+a):
	for j in range(i,0,-1):
		temp=max(dp[j],dp[j-1]+potions[i-1])#喝j-1瓶加上第i瓶
		if temp>=0:#注意排除负数
			dp[j]=temp
for i in range(a,-1,-1):#倒序，输出序号最大的一个
	if dp[i]>=0:
		print(i)
		break'''

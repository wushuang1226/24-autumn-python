#自己写的问题在于，这道题d在变就没有设保护圈，但是有可能投在边上跟中间一样多！
#所以用max min 写保护圈也要会！
q=1025
d=int(input())
n=int(input())
dp=[[0]*q for i in range(q)]
for k in range(n):
    x,y,i=map(int,input().split())
    #第二种保护圈！
    for dx in range(max(x-d,0),min(1025,x+d+1)):
        for dy in range(max(0,y-d),min(1025,y+d+1)):
            #双向思维，每个垃圾周围d能炸到i
            dp[dx][dy]+=i
'''c=[]
for i in range(q):
    c.append(max(dp[i]))
#变量名重了嘞d=max(c)
e=max(c)
print(c.count(e),e)每行不一定一个最大值嘞'''
#善用括号内循环
maxk = max(max(l) for l in dp)
num = sum(l.count(maxk) for l in dp)
print(num, maxk)
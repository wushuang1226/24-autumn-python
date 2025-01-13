#多重背包 二进制分组
n=int(input())#公因数
if n%50!=0:
    print("Fail")
    exit()
n//=50
a=list(map(int,input().split()))
c=[1,2,5,10,20,50,100]
'''b=[]
for y in range(7):
    b+=[c[y]//50]*a[y]'''
#print(b)
dp=[0]+[float("inf")]*(n)#0==0 or 1!
for j in range(7):
    cur_price=c[j]
    left_num=a[j]
    k = 1
    while left_num > 0:
        use_num=min(left_num, k)
        k *= 2
        left_num -= use_num
        for i in range(n, cur_price * use_num - 1, -1):
            if dp[i - cur_price * use_num] != float("inf"):#用其他的会影响数。
                dp[i]=min(dp[i-cur_price * use_num]+use_num,dp[i])
#print(dp)
if dp[-1]==float("inf"):
    print('Fail')
else:
    print(dp[-1])

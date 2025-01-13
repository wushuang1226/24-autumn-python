#continue dp (ending by "K")
#20+
#tl,wa
a=list(map(int,input().split(',')))
n=len(a)
dp=[0]*n
last_min=0
cur_min=0
#这两个变量代表不取的那个最小值，如果都取则为0
dp[0]=a[0]
for i in range(1,n):
        cur_min=min(last_min,a[i])
        #print(cur_min,last_min)
        dp[i]=max(a[i],a[i]+dp[i-1]+last_min-cur_min)
        if a[i]>a[i]+int(dp[i-1])+last_min-cur_min:
            last_min=min(0,a[i])
        else:
            last_min=cur_min
#eg10,-100,1,-2,110,-101,200
#会被前面的连续困住
print(dp)
print(max(dp))

#dp——0-1背包!!!
#str VS int 比大小
#跟最大最小整数类似 规避898 8987的情况！
m=int(input())
n=int(input())
a=list(input().split())
#a.sort(reverse=True)
#先greedy排序，再dp！dp只是起到限制位数 可以用两倍最大长度 or 直接乘10倍比较
#法二 冒泡排序
for i in range(n):
    for j in range(n-i-1):
        if a[j]+a[j+1]<a[j+1]+a[j]:
            a[j],a[j+1]=a[j+1],a[j]
#print(a)

#避免重复：滚动数组逆向遍历 or 添加temp=dp[:]缓存
dp=[0]*(m+1)
for j in a:
    for i in range(m,len(j)-1,-1):
        if i-len(j)==0 or dp[i-len(j)]!=0:
            dp[i]=max(dp[i],int(str(dp[i-len(j)])+j))
#print(dp)
print(dp[-1])


#（）25 is very small
#现学现卖一下教材
#最长下降子序列
k=int(input())
a=list(map(int,input().split()))
longest=[1]*k

for i in range(k):
    for j in range(i):
        if a[j]>=a[i]:#取等！！！
            longest[i]=max(longest[j]+1,longest[i])
print(max(longest))

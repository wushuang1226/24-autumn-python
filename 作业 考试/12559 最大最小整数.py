
n=int(input())
a=list(input().split())

'''i=0
while i<n-1:#用上n。
    if a[i] in a[i+1]:
        if int(a[i][0])>int(a[i+1][-1]):
            a[i],a[i+1]=a[i+1],a[i]
    i+=1
b=tuple(a)#否则连带改变
相邻互换效率很低，且无法来回换，基本上WA
'''
#没有考虑到提示的特殊情况
#期末考试考虑两个互换即可？咋可能。

#位数不足，重新从第一位开始比
from math import ceil
max_len=len(max(a,key= lambda x:len(x)))
a.sort(key=lambda x:x*ceil(2*max_len/len(x)))#为什么要乘二倍？
b=a#True是倒序
c=b[::-1]#倒序
print(''.join(c),''.join(b))
#好好利用样例！！！
n=int(input())
a=list(input().split())
b=0
for i in range(len(a)-1):
    if b+len(a[i])+1+len(a[i+1])>80:
        #中间的空格别落下
        print(a[i])
        b=0
    else:
        print(a[i],end=" ")
        b+=len(a[i])+1
        #空格也要算上字符数
print(a[-1])
#'\n'.join(a)

#感觉上先建表会省时间
#10**7是k的范围，不是n！！
a=[0]*(1000000+1)
a[0]=1
a[1]=2
for i in range(2,len(a)):
    a[i]=(a[i-1]*2+a[i-2])%32767
    #数据太大，仅考虑余数即可

n=int(input())
for i in range(n):
    k=int(input())
    print(a[k-1]%32767)
#-1-1-1-1!

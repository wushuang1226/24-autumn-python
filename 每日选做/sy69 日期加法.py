#数据较少，一个月一个月加，12元素列表，2月更新

y,m,d=map(int,input().split('-'))
n=int(input())
y1=y+n//365
n1=n%365+d
#闰年………整百
if y%4==0 and y!=1900 and y!=y1:
    if m<=2:
        n1-=1
#关注第一年 同一年等特殊情况
for i in range(y+1,y1):
    if i%4==0:
        n1-=1
big=[1,3,5,7,8,10]
small=[4,6,9,11]
while True:
    if m in big and n1-31>0:
        n1-=31
        m+=1
    elif m in small and n1-30>0:
        n1-=30
        m+=1
    elif m==2 and y1%4==0 and n1-29>0:
        n1-=29
        m+=1
    elif m == 2 and y1 % 4 != 0 and n1 - 28 > 0:
        n1 -= 28
        m += 1
    elif m==12 and n1-31>0:
        n1-=31
        m=1
        y1+=1
    else:
        break
print('%d-%s-%s'%(y1,str(m) if m>9 else"0"+str(m)\
                      ,str(n1) if n1>9 else"0"+str(n1)))
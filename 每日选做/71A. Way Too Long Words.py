n=int(input())
for i in range(n):
    a=input()
    if len(a)<=10:
        print(a)
    else:
        print(a[0],len(a)-2,a[-1],sep='')
#print内部条件判断：print(a if l<11 else a[0]+str(l-2)+a[l-1])
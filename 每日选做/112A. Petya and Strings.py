a=input().lower()
b=str(input().lower())
n=len(a)

c=0
for x in range(n):
    if a[x]>b[x]:
        c=1
        break
    elif a[x]<b[x]:
        c=-1
        break
    else:
        pass

if c==1:
    print('1')
elif c==-1:
    print('-1')
else:
    print('0')

#其实无需一位一位比较

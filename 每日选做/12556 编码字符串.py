a=input().lower()
n=len(a)
b=1
for i in range(n-1):
    if a[i]==a[i+1]:
        b+=1
    else:
        print('(',end='')
        print(a[i],end='')
        print(',',end='')
        print(b,end='')
        print(')',end='')
        b=1
print('(',end='')
print(a[-1],end='')
print(',',end='')
print(b,end='')
print(')',end='')
#字符串格式化
#+=1用首尾代替
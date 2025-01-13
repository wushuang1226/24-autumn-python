n=int(input())
a=list(input())
b=0
for i in range(n-1):
        if a[i]==a[i+1]:
            b=b+1
print(b)
#由于一开始做错了折腾了快半个小时……

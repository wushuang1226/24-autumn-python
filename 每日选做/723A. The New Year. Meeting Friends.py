a,b,c=map(int,input().split())
d=(a+b)/2
e=d+(c-d)/3
print(int(abs(a-e)+abs(b-e)+abs(c-e)))
#最大减去最小！在中间人汇合
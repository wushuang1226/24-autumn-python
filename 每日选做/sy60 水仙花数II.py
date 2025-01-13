a,b=map(int,input().split())
n=0
e=[]
for i in range(a,b+1):
#左闭右开
    c=[int(x) for x in str(i)]
    d=[y**3 for y in c]
#    cubed = map(lambda x: x**3, numbers)
    if i==sum(d):
        #print(i,end=" ")行末不允许有多余空格！
        e.append(str(i))
        n=1
if n==0:
    print("NO")
else:
    print(" ".join(e))


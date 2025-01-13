l,n,m=map(int,input().split())
a=[int(input()) for i in range(n)]
a.insert(0,0)
a.append(l)
b=[[a[i]-a[i-1],a[i+1]-a[i],i]for i in range(1,n)]
b.sort(key=lambda x:(min(x[0],x[1]),max(x[0],x[1])))
a0=[b[i][2] for i in range(m)]
a1=[a[j] for j in range(n+2) if j not in a0]
    #切忌一边循环一边删！！序号会变a.pop(b[i][2])
b1=[min(a1[i]-a1[i-1],a1[i+1]-a1[i])for i in range(1,n-m)]
#print(a1,b1)
print(min(b1))

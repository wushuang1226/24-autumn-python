import bisect
a=list(map(int,input().split()))
n=len(a)
b=[0]*(n)
peak=[]
for i in range(1,n):
            if a[i]>a[i-1]:
                b[i]=1
            elif a[i]<a[i-1]:
                b[i]=-1
                peak.append(i-1)
            else:
                peak.append(i)
c=[1]*n
for i in range(1,n):
            if b[i]==1:
                c[i]=c[i-1]+1
            if b[i]==-1:
                if c[i-1]>=2:
                    c[i]=c[i-1]-1
                else:
                    for k in range(peak[bisect.bisect(peak,i)-1],i):
                        c[k]+=1
print(peak,b,c)

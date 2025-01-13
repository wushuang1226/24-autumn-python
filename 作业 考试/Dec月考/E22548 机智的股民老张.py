#15min
#don't be anxious! EASY
a=list(map(int,input().split()))
n=len(a)
ans=[0]
bottom=a[0]
for i in range(1,n):
    if a[i]>=bottom:
        ans.append(a[i]-bottom)
    if a[i]<bottom:
        bottom=a[i]

#print(ans)
print(max(ans))
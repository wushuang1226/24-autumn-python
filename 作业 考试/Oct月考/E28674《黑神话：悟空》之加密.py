#20min
a='abcdefghijklmnopqrstuvwxyz'
k=int(input())
k=k%26
s0=input()
s=s0.lower()
b=[]
for i in s:
    for j in a:
        if j==i:
            if a.index(j)-k<0:
                i=a[a.index(j)-k+26]
                b.append(i)
                break
            else:
                i = a[a.index(j) - k ]
                b.append(i)
                break
b0=''.join(b)

for i in range(len(s0)):
    if s0[i]<'a':
        b[i]=b0[i].upper()
print(''.join(b))


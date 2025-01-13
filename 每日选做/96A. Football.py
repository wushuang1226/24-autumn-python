a=input()
b=1
c=0
for i in range(len(a)-1):
    if b>=7:
        c=1
        break
    if b==6 and i==len(a)-2:
        c=1
    if a[i]==a[i+1]:
        b=b+1
    else:
        b=1
if c==1:
    print("YES")
else:
    print("NO")

'''法二 由于只有1和0，直接分类
        if c=='0':
                n_0 += 1
                if n_0==7: break
                n_1 = 0
        else:
                n_1 += 1
                if n_1==7: break
                n_0 = 0

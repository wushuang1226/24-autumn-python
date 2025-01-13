n=str(bin(int(input())))
#二进制开头有0b 用print自查！
l=list(n[2:])
m=[0]*(len(n)-2)
for i in range(len(n)-2):
    m[len(n)-i-3]=l[i]
if l==m:
    print("Yes")
else:
    print("No")


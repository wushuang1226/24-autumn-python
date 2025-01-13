t=int(input())
for i in range(t):
    a=input()
    n=len(a)-a.count('0')
    print(n)
    for j in range(len(a)):
        if a[j]=="0":
            continue
        else:
            print(int(a[j])*10**(len(a)-j-1),end=" ")
    print()
#15min
#for j in a

n=int(input())
x=0
for i in range(n):
    a=input()
    if a.count("+")!=0:
        x+=1
    else:
        x-=1
print(x)
'''f=input
True==-1,False==0
print(sum('+'in f() or -1 for i in range(int(f()))))'''
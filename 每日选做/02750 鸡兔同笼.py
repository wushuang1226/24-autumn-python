a=int(input())
if a%2==0:
    if a%4==0:
        less=a/4
        print(int(less),end=" ")
    else:
        less=(a+2)/4
        print(int(less),end=" ")
    more=a/2
    print(int(more))
else:
    print(0,end=" ")
    print(0)

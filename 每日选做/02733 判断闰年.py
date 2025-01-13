a=int(input())
if a%4==0:
    if a%100!=0:
        print("Y")
    else:
        if a%400==0:
            print("Y")
        else:
            print("N")
else:
    print("N")

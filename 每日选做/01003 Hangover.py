while True:
    n=float(input())
    if n==0:
        break
    a=0
    i=2
    while True:
        a+=1/i
        i+=1
        if a>n:
            break
    print(i-2,'card(s)')
#是整数就打整数
#break 与 While True搭配可以嵌套
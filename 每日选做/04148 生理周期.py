    #数据不算太大先打表试试
#简单粗暴的遍历答案：    while (s-p)%23 !=0 or (s-e)%28 != 0 or (s-i)%33 !=0 :

    #三重循环很显然自己跑都大大超时喽
c=1
while True:
    p,e,i,d=map(int,input().split())
    if p==-1:
        break
    p0=[p%23+23*i for i in range(1,925)]
    e0=[e%28+28*i for i in range(1,760)]
    i0=[i%33+33*j for j in range(1,645)]
    #不要用一样的变量名嘞
    '''k=1
    while k:
        print(1)
        for x in p0[:d//23:-1]:
            while k:
                for y in e0[:d//28:-1]:
                    for z in i0[:d//33:-1]:
                        if x==y==z:超慢的循环
                        print
                        k=0利用参数跳出多层循环
                        break只跳过最内层'''
    a=set(p0)&set(e0)&set(i0)
    # 被集合的速度震撼
    for i in a:
        if i > d:
            print(f'Case {c}: the next triple peak occurs in {i-d} days.')
    c+=1
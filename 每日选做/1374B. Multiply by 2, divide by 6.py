
t=int(input())
for i in range(t):
    a=0
    n=int(input())
    while n!=1:
        if n%6==0:
            n/=6
            a+=1
        elif n%3==0:
            n/=3
            a+=2
        else:
            a=-1
            break#别忘记 要不就无限循环啦
    print(a)

'''while True:
        if n==1:
            break
            不太行……break会跳出总循环'''

        
    
        

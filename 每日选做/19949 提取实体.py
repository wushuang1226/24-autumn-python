n=int(input())
b=0
for i in range(n):
    a=input()
    b+=a.count('###')/2-a.count('### ###')
    #ans += (input().replace('### ###', '')).count('###') // 2整除？
print(int(b))
#缩进！整篇or每行

    

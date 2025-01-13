n=int(input())
print('*')
print('**')
if n==3:
    print("***")
elif n>3:
    print('* *')
    for i in range(3,n-1):
        print('*',' '*(i-3),'*')
        #将逗号改为加号 可以省去行内空格 也不用再分类
    print('*'*n)
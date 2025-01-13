#二维数表一维化，写出每一行皇后所在的列数（默认行不相同）
#也是自己敲了一遍答案。
list1=[]

def q(s):
    if len(s)==8:
        list1.append(s)
        return
    else:
        for i in range(1,9):#新一行列数
            if all(s[j]!=str(i) and abs(i-int(s[j]))!=abs(j-len(s)) for j in range(len(s))):#行差不等于列差
                q(s+str(i))#重复调用自身
q('')

samples = int(input())
for k in range(samples):
    print(list1[int(input()) - 1])
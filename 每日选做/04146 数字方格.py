'''#23随便分配 2奇偶可调？a23=2n不可以
#不会有无用的条件嘞
#eg 3,5多试几组！
n=int(input())
a123=(n*3//5)*5
x=a123+5
y=n*3-a123
a=0
while a==0:
    x-=5
    for i in range(x//3+1,n+1):
        if (x-i)%3==0:
            if x-i!=2*n:
                a=1
            else:
                if(x-i+n)%2==0:
                    a=1'''

#.......100的数据量直接遍历就好啦，以后也先试遍历
n = int(input())
m=0
for i in range(n, -1, -1):
    for j in range(n, -1, -1):
        for k in range(n, -1, -1):
            if (i + j) % 2 == 0 and (j + k) % 3 == 0 and (i + j + k) % 5 == 0:
                m=max(m,i+j+k)
print(m)
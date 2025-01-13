n=int(input())
a=""
if n==1:
    print("I hate it")
elif n==2:
    print('I hate that I love it')
elif n%2==1:
    print('I hate ','that I love that I hate '*(n//2),'it',sep='')
else:
    print('I hate that I love ','that I hate that I love '*(n//2-1),'it',sep='')
'''say = []
for i in range(int(input())):
    say.append(['I hate', 'I love'][i % 2])
print(" that ".join(say), end=" it")
不用对总数分类，奇偶逐一加上即可'''
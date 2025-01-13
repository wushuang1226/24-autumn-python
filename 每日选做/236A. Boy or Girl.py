a=list(input())
b=set()
for i in range(len(a)):
    b.add(a[i])
if len(b)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

#简：s = set();s.update(input())

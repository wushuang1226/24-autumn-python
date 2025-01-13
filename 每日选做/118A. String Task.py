a=list(input())
#开头就lower更简便
v=["A", "O", "Y", "E", "U", "I",'a','o','y','e','u','i']
c=[]
for i in a:
    if i not in v:
        c.append(i)
        #添加优于删除，否则遍历会受影响
b='.'.join(c)
print('.',b.lower(),sep='')
#print(''.join('.'+l for l in input().lower() if l not in 'aeiouy'))

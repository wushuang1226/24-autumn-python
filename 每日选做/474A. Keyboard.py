k=['q','w','e','r','t','y','u','i','o','p','[',\
   'a','s','d','f','g','h','j','k','l',';',\
   'z','x','c','v','b','n','m',',','.','/']
#直接写成一个字符串
#k[k.index(i)+-1]
a=input()
b=input()
c=[]
if a=="L":
    for i in b:
        for j in range(len(k)):
            if i==k[j]:
                c+=k[j+1]
else:
    for i in b:
        for j in range(len(k)):
            if i==k[j]:
                c+=k[j-1]
print(''.join(c))

s=input()
a=s.find('h')
b=s.find('e',a,len(s)+1)
c=s.find('l',b,len(s)+1)
d=s.find('l',c+1,len(s)+1)
e=s.find('o',d,len(s)+1)
if a!=-1 and b!=-1 and c!=-1 and d!=-1 and e!=-1:
    print("YES")
else:
    print("NO")
'''
s=input()
data = 'hello'
cnt = 0
遍历是按顺序的
for c in s:
    if c == data[cnt]:
        cnt += 1
由答案简化了一些xixi
    if cnt == 5:
        print("YES")
        break
else:
    print('NO')'''
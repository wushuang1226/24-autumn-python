#字典的使用
n,k=map(int,input().split())
d={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
a=[]
i=1
if n==1:
    print(1)
while k**i<n:
    i+=1
for j in range(i,-1,-1):
    a.append(n//(k**j))
    n=n%(k**j)

while a[0]==0:
    a=a[1:]
for i in range(len(a)):
    if a[i] in d:
        a[i]=d[a[i]]
    a[i]=str(a[i])

print(''.join(a))
'''if n == 0:
    k_representation = "0"
else:
    while n > 0:
        k_representation = str(dic[n % k]) + k_representation
        n //= k类似短除法转化二进制
        余数反写'''


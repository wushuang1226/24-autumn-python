a=list(input())
b=a[0]
a[0]=b.capitalize()

for i in range(len(a)):
    print(a[i],end="")
    
#print(line[0].upper() + line[1:])

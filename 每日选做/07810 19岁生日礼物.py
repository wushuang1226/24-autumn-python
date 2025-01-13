
def nineteen(n):
    if int(n)%19==0:
        return "Yes"
    for i in range(len(n)-1):
        if n[i:i+2]=='19':
            return 'Yes'
    return"No"

n=int(input())
for i in range(n):
    p=input()
    print(nineteen(p))
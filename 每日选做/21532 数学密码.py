n=int(input())
for i in range(n//6,0,-1):
    if n%i==0:
        print(i)
        break
"""n=int(input())
i = 1 + 2 + 3
while n%i != 0:
    i += 1
else:
    print(n // i)
    从小到大更好"""
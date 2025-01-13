a=list(input())

for i in range(len(a)):
    if a[i].islower():
        a[i]=a[i].upper()
    else:
        a[i]=a[i].lower()
print(''.join(a))
#ans += chr(ord(i) + gap)
#[]+=i

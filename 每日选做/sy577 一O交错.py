s=input()
a=1
b=[1]
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        a+=1
    else:
        b.append(a)
        # 逐一替代max_length = max(max_length, current_length)
        a=1
b.append(a)
print(max(b))
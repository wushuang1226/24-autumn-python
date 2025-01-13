m=int(input())
for i in range(m):
    a,b,c,d=map(int,input().split())
    if a+b+c+d==24 or a+b+c-d==24 or a+b-c+d==24 or a+b-c-d==24 \
       or a-b+c+d==24 or a-b+c-d==24 or a-b-c+d==24 or a-b-c-d==24 \
       or -a+b+c+d==24 or -a+b+c-d==24 or -a+b-c+d==24 or -a+b-c-d==24 or \
       -a-b+c+d==24 or -a-b+c-d==24 or -a-b-c+d==24 or -a-b-c-d==24:
        print('YES')
        #and or条件写完整
    else:
        print('NO')        

'''避免重复：循环嵌套
	a,b,c,d = [int(num) for num in input().split()]
	flag = False
	for j in [a, -a]:
		for k in [b, -b]:
			for l in [c, -c]:
				for m in [d, -d]:
					if j + k + l + m == 24:
						flag = True
	print('YES' if flag else 'NO')'''

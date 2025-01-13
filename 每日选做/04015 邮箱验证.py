while True:
        try:
                a = input()
        except EOFError:
                break
#未知若干行应该怎么处?
        i=a.find('@')
        j=a.find('.')
        if a.count('@')!=1:
            print('NO')
        #直接找，不会出现-1！elif i==0 or j==0 or i==-1 or j==-1:
        elif a[0] in ['@','.'] or a[-1] in ['@','.']:
            print('NO')
        elif a[i:].count('.')<1:
            print('NO')
        elif a[i+1]=='.'or a[i-1]=='.':
        #可能有多个点 所以不能直接用j
        #相邻……前后
            print('NO')
        else:
            print("YES")
            

        
            

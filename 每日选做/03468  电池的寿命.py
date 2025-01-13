#例题一次炸鸡排一次叻。。能自己做不。。
while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        t = sum(a)
        if a[-1] > t / 2:
            print('%.1f'%(sum(a) - a[-1]))
        else:
            print(('%10.1f' % (t/2)).strip())
    except EOFError:
        break


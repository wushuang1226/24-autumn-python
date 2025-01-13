'''
初步分析：最理想时长等于n/2
极端入手：最长的与剩余之和比较（若小于等于，则猜测可以满足）
调整法：每次把最长的用一个小时（关注整数条件，别想得太复杂），之后a[n]-1或a[n-2]最大，（1,1,1）为特例，但易构造发现仍然满足'''
while True:
        try:
            n = int(input())
            a = list(map(int, input().split()))
            b=max(a)
            if b<=(sum(a)-b):
                print(round(float(sum(a)/2),1))
            else:
                print(round(float(sum(a)-b),1))
        except EOFError:
                break


#25min RT
'''sign = 1
if tokens[0]=="negative":
    sign = -1
    del tokens[0]

total = 0
tmp = 0
for i in tokens:
    if i in ("thousand", "million"):
        total += tmp*dic[i]
        tmp = 0
        continue
    if i == "hundred":
        tmp *= dic[i]
    else:
        tmp += dic[i]

print( sign * (total + tmp) )更简介的写法'''
a=list(input().split())
sign=1
am=[]
at=[]

if a[0]=='negative':
    sign=-1
    a.remove(a[0])
if 'million' in a:
    am=a[:a.index('million')]
    a=a[a.index('million')+1:]
if 'thousand' in a:
    at=a[:a.index('thousand')]
    a=a[a.index('thousand')+1:]
d={'zero':0,'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8 ,'nine':9, 'ten':10, 'eleven':11, 'twelve':12,'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}

def part(a):
    k=0
    if 'hundred' in a:
        ah = a[:a.index('hundred')]
        a = a[a.index('hundred') + 1:]
        for i in ah:
            k+=d[i]*100
        for i in a:
            k+=d[i]
    else:
        for i in a:
            k+=d[i]
    return k
print(sign*(part(am)*1000000+part(at)*1000+part(a)))
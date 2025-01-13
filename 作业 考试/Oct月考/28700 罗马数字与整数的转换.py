#30min WA
#第一次让AI帮忙找了一组错误数据，很有效！
#先查书写错误。。。。。
a=input()
#看提示
b=[i for i in range(10)]
b0=[str(i) for i in b]
if a[0] in b0:
    a=int(a)
    d=[]
    d.append(a//1000*'M')
    a=a%1000
    if a>=900:
        d.append("CM")
        a-=900
    elif a>=500:
        d.append("D")
        a-=500
    elif a>=400:
        d.append("CD")
        a-=400
    d.append(a // 100 * 'C')
    a = a % 100
    if a>=90:
        d.append("XC")
        a-=90
    elif a>=50:
        d.append("L")
        a-=50
    elif a>=40:
        d.append("XL")
        a-=40
    d.append(a // 10 * 'X')
    a = a % 10
    if a>=9:
        d.append("IX")
        a-=9
    elif a>=5:
        d.append("V")
        a-=5
    elif a>=4:
        d.append("IV")
        a-=4
    d.append(a  * 'I')
    print(''.join(d))
else:
    d=0
    for i in a:
        if i=='M':
            d+=1000
        if i=="D":
            d+=500
        if i=="C":
            d+=100
        if i=="L":
            d+=50
        if i=="X":
            d+=10
        if i=="V":
            d+=5
        if i=="I":
            d+=1
    d-=a.count('IV')*2+a.count('IX')*2+a.count('XL')*20+a.count("XC")*20+a.count('CD')*200+a.count('CM')*200
    print(d)
'''
简便：
# 定义罗马数字和整数的映射关系
roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# 定义整数到罗马数字的映射列表 (从大到小顺序)
int_to_roman_map = [ (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

# 罗马数字转整数
def roman_to_int(s):
    total = 0
    prev_value = 0
    for char in s:
        value = roman_to_int_map[char]
        if value > prev_value:
            total += value - 2 * prev_value  # 处理特殊情况，如IV, IX
        else:
            total += value
        prev_value = value（上一位）
    return total

# 整数转罗马数字
def int_to_roman(num):
    result = []
    双变量循环！
    从大到小
    for value, symbol in int_to_roman_map:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)

# 主函数，判断输入是罗马数字还是整数
'''


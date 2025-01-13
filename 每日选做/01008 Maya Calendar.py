n=int(input())
#都对答案了还把这行忘了也太蠢啦。。
print(n)
H_month={'pop':1, 'no':2, 'zip':3, 'zotz':4, 'tzec':5, 'xul':6, 'yoxkin':7, 'mol':8, 'chen':9, 'yax':10, 'zac':11, 'ceh':12, 'mac':13, 'kankin':14, 'muan':15, 'pax':16, 'koyab':17, 'cumhu':18,"uayet":19}
T_month={1:'imix',2: 'ik', 3:'akbal',4:'kan', 5:'chicchan', 6:'cimi', 7:'manik', 8:'lamat', 9:'muluk', 10:'ok', 11:'chuen', 12:'eb', 13:'ben', 14:'ix', 15:'mem', 16:'cib', 17:'caban', 18:'eznab', 19:'canac', 0:'ahau'}
for i in range(n):
    Hd,Hm,Hy=input().split()
    Hd=int(Hd[:-1])
    Hm=H_month[Hm]
    Hy=int(Hy)
    day=Hy*365+(Hm-1)*20+(Hd+1)
    if day%260==0:
        Ty = day // 260-1
    else:
        Ty=day//260
    #关注0.
    day=day%260
    if day%13==0:
        Td=13
    else:
        Td=day%13
    Tm=T_month[day%20]
    print(str(Td),Tm,str(Ty))

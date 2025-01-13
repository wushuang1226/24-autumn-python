a=[]
for i in range(3,363):
    if (180*(i-2)/i)%1==0:
        a.append(180*(i-2)/i)

for i in range(int(input())):
    b=int(input())
    print(["NO","YES"][b in a])
    #补角……360%(180-b)==0
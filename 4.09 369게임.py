print("10이상 1000이하의 정수 하나를 입력하시오")
N=int(input())

for i in range(1,N+1):
    r=0
    on=int(i%10)
    tn=int(i/10)
    tn=int(tn%10)
    hn=int(i/100)
    
    if i<10:
        if on%3==0:
            r=r+1
    if i>=10 and i<100:
        if tn%3==0:
           if (on%3==0 and on!=0):
               r+=2
           else :
               r=r+1
        else:
            if (on%3==0 and on!=0):
                r=r+1
    if(r == 1):         
        print('-')
    elif(r==2):
        print('--')
    else:
        print(i)

        
        

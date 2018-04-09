print("초기값 하나를 입력하세요")
sn=int(input())

def multi(a):    
    print("숫자하나를 더 입력하세요")
    b=int(input())
    return a*b

def add(a):
    print("숫자하나를 더 입력하세요")
    b=int(input())
    return a+b
    
def divide(a):
    print("숫자하나를 더 입력하세요")
    b=int(input())
    return a/b
    
def minus(a):
    print("숫자하나를 더 입력하세요")
    b=int(input())
    return a-b
   
while True:
        print("1~5까지의 옵션 중 하나를 선택하세요")
        a=int(input())
        if a==1:
            sn = multi(sn)
        if a==2:
            sn = add(sn)
        if a==3:
            sn =divide(sn)
        if a==4:
            sn = minus(sn)
        if a==5:
            print("최종값은",sn,"입니다")
            break


        
            

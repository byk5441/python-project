print("네자리 숫자를 입력하시오")
mynum=int(input())


def tot(num):
    
    a= int(num/1000)
    b=int((num-1000*a)/100)
    c=int((num-1000*a-100*b)/10)
    d=int((num-1000*a-100*b-10*c))

    fsum = a+b+c+d

    return fsum

def mx(num):
    a= int(num/1000)
    b=int((num-1000*a)/100)
    c=int((num-1000*a-100*b)/10)
    d=int((num-1000*a-100*b-10*c))

    mx=a
    if(b>mx):
        mx=b
    if(c>mx):
        mx=c
    if(d>mx):
        mx=d
    return mx


print (tot(mynum))
print (mx(mynum))

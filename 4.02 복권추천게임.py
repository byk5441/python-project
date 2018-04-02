import random
num=0

while True:

    a= int (random.randint(1,8))

    b= int (random.randint(9,16))

    c= int (random.randint(17,24))

    d= int (random.randint(25,32))

    e= int (random.randint(33,40))

    f= int (random.randint(40,45))

    if a==3 and b==11 and c==19 and d==27 and e==38 and f==43 :
        num=num+1
        break

    else:
        num=num+1
    

print (num)


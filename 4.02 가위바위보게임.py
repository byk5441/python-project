import random
gamelist
cpt=random.choice(gamelist)
while True:

    print("가위바위보중에서 하나를 골라주세요")
    a=input()
    if (a=='가위'and cpt=='보') or (a=='바위' and cpt=='가위')or (a=='보' and cpt =='바위'):
            print("당신이 이겼습니다")
            break
    
      


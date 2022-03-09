class Unit:
    def __init__(self,name, hp, damage):
        self.name = name
        self.hp= hp
        self.damage = damage
        print("{0} Unit has been created.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린",40 , 5)
marine2 = Unit("마린",40 , 5)
tank =Unit("Tank",150,36)


#__init__ 생성자. 객체가 생성될 때 init 함수와 동일하게 생성. 
# 멤버 변수: 클래스내에서 생성된 변수 .  

#레이스 

wraith1= Unit("wraith", 80,5)
wraith2= Unit("Wraith",80,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} Clocking".format(wraith2.name))  #변수를 추가로 만들어서 외부에서 사용 가능. 
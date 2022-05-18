from turtle import speed


class Unit:
    def __init__(self,name, hp):
        self.name = name
        self.hp= hp
        self.speed = speed
    
    def move(self, location):
        print("지상 유닛 이동")
        print('{0} : {1} 방향으로 이동합니다. 속도 {2}')\
            .format(self,name, location, self.speed)
#         self.damage = damage
#         print("{0} Unit has been created.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린",40 , 5)
# marine2 = Unit("마린",40 , 5)
# tank =Unit("Tank",150,36)


#__init__ 생성자. 객체가 생성될 때 init 함수와 동일하게 생성. 
# 멤버 변수: 클래스내에서 생성된 변수 .  

#레이스 

# wraith1= Unit("wraith", 80,5)
# wraith2= Unit("Wraith",80,5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} Clocking".format(wraith2.name))  #변수를 추가로 만들어서 외부에서 사용 가능. 

class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self, name, hp, speed)
        self.damage= damage

    def attack(self, location):
        print("{0}:{1} 방향으로 공격 합니다. [공격력 {2}]"\
            .format(self.name,location,self.damage))

    def damaged(self, damage):
        print({"{0} : {1} 데미지를 입었습니다.".format(self.name, damage)})
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))


# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다.[속도 {2}]".\
            format(name,location,self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name, hp,0, damage)
        Flyable.__init__(self,flying_speed)


valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name, "3시")

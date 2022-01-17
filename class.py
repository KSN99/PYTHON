#class란? 함수와 변수들의 합 함수+변수
#object란? 클래스를 이용하여 만든 물체
#object== instance 

class Person:
    def __init__(self,name,age):
 #init person 이라는 오브젝트를 만들 때 네임이라는 인자를 받아서 네임이라는 변수안에 그 값을 넣어라
        self.name=name
        self.age=age
    def say_hello(self,to_name):
        print("Hi!"+to_name+"I'm"+self.name)
        #만들어진 물체에 변수를 활용해야 할 떄
        #self 인자 사용 
    def introduce(self):
        print("My name is"+self.name+" and I am "+str(self.age))
p= Person("WW",24)
p.say_hello("ZZ")
p.introduce()
k= Person("K",25)
k.say_hello("*")
k.introduce()

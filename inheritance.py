#상속은 공통된 클래스가 하나 있고 그밑에 여러 세부 클래스들을 만들고 싶을 때 

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


class Police(Person): #상속은 중복으 ㅣ제거 가능. 
    def arrest(self,to_arrest):
        print("You are arested "+ to_arrest)

class Programmer(Person):
    def program(self,to_program):
        print("What am I gonna program: "+to_program)

p= Person("WW",24)
jenny= Police("jenny",21)
michael= Programmer("michael",28)

p.introduce()
jenny.introduce()
michael.introduce()
jenny.arrest("p")
michael.program("Python")
#어떤 기능들을 구현하는 모듈들의 합 
#라이브러리 == 패키지 (파이썬)
#패키지= 모듈1+모듈2 
#모듈이란 ? 코드를 모아서 기능하나를 구현해놓은 파일 
# 모듈== 코드가 들어있는 파일? 이코드가 모여서 어떤 한 기능을 구현


# animal package 
# dog, cat modules
# dog, cat modules can say "hi "

from animal import dog #animal 패키지에서 dog라는 모듈을 불러오는 것
from animal import cat 

from animal import * # animal 패키지에서 갖고있는 모듈을 전부 불러와.

d= Dog()
c= Cat()

d.hi()
c.hi()
# d = dog.Dog() #insatance
# d.hi()

# c= cat.Cat()
# c.hi()
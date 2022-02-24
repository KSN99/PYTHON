#print(abs(-5)) # 절댓값
#print(pow(4,2)) # 4^2 = 4*4 = 16 
#print(max(5,12)) # 최댓값 출력 
#print(min(5,12))  # 최솟값 출력 
#print(round(4.99)) # 반올림 

#from math import *
#print(floor(4.99)) #내림 
#print(ceil(3.14)) #올림
#print(sqrt(16)) #제곱근

from random import * #랜덤함수 . 

print(random()) #0.0 이상 ~ 1.0 미만의 값 생성 
print(random() *10) # 0.0 ~ 10
print(int(random()*10)) #1~ 10 미만
print(int(random()*10)+1) # 1~ 10 이하

print(randrange(1,46)) # 1~ 45 이하
print(randint(1,45)) 



date= randint(4,28)

print("오프라인 스터디 모임 날짜는 매월"+ str(date)+"afds")
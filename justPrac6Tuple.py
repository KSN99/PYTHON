#Tuple 
# 속도가 리스트보다 빠름

menu = ("A","B")
print(menu[0])
print(menu[1])

#tuple 은 add 불가능 값 추가 변경 x 

name = "김종국"
age = 20
hobby = "coding"
print(name, age,hobby)

(name,age,hobby) = ("김종국",20,"coding")
print(name,age,hobby)
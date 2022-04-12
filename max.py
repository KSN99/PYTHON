# 세 정수 입력받아 최댓값 구하기 

print("세 정수의 최댓값을 구합니다.")
a= int(input("INT a:"))
b= int(input("Int b:"))
c= int(input("int c:"))

maximum =a
if b > maximum: maximum= b
if c > maximum: maximum= c

print(f'최댓값은 {maximum}.')

# 세 정수 입력받아 최댓값 구하기 

print("세 정수의 최댓값을 구합니다.")
a= int(input("INT a:"))
b= int(input("Int b:"))
c= int(input("int c:"))

maximum =a
if b > maximum: maximum= b
if c > maximum: maximum= c

print(f'최댓값은 {maximum}.')

#순차 구조 
# 조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경되는데 이러한 구조를 선택 구조 (select structure) 이라고 함. 

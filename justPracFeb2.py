#문자열 처리함수 
python = "python is amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # False 출력 
print(len(python))
print(python.replace("python","seongnyeon"))

index = python.index("n")
print(index)

index = python.index("n", index+1)
print(index)

print(python.find("n"))

print(python.find("Java")) #원하는 값 없을 때 -1 반환
#print(python.index("Java")) # 원하는 값 없을 때 오류 발생 후 프로그램 종료 . 

print(python.count("n"))
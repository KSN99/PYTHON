# 먼저 이름과 나이를 받고
#나이가 10살 미만이면 안녕이라고 말하기
#나이가 10살에서 20살 사이면 안녕하세요 라고 
# 그외에는 안녕하십니까 라고 말하기 

def greeting(name,age):
    if age < 10:
        print("안녕"+name)
    elif age <=20 and age >= 10:
        print("hi"+name)
    else:
        print("Hello"+name)

greeting("k",10)
greeting("alex",20)
greeting("brina", 40)

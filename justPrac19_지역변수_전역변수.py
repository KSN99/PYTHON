#함수내에서만 쓰는 >> 지역변수 
#프로그램 전체에서 >> 전역변수 

gun = 10

def checkpoint(soldiers):
    global gun #전역 공간에 있는 gun 사용 . 
    gun= gun- soldiers
    print("[함수내] 남은 총: {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun=gun-soldiers
    print("[함수내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
gun= checkpoint_ret(gun,2)

#checkpoint(2)
print("남은 총:{0}".format(gun))
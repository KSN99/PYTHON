# 세 정수를 입력받아 중앙값 구하기 1

def med3(a,b,c):
    if (b >=a and c<=a) or (b <= a and c>=a):
        return a

    elif ( a>b and c<b) or (a<b and c>b):
        return b
    
    return c 
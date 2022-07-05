try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1=int(input("first num:"))
    num2=int(input("second num:"))
    if num1>=10 or num2>=10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))

except ValueError:
    print("wrong number 한 자리 숫자만 가능.")
# + 와 - 번갈아 출력하기 2
 
print('+- print.')
n= int(input('몇 개를 출력할까요?'))

# 파이선에서는 무시하고싶은 값을 언더스코어로 표현할 수 있음. range 함수가 for문을 
#순환하며 반환하는값 (인덱스)를 사용할 필요가 없기때문. 
for _ in range(n//2):
    print('+-', end='')

if n%2:
    print('+',end='')


print()
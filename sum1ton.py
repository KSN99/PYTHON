# 변수가 하나일 때는 while 문보다 for문을 사용하는 것이 더 좋다. 
# 1부터 n까지의 정수의 합 구하기 2 (for문)

print('1부터 n까지 정수의 합')
n=int(input('n:'))

sum=0
for i in range(1,n+1):
    sum+=i

print(f'1부터 {n}까지 합은 {sum}.')

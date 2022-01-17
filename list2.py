x= [4,2,3,1]
#반복문 리스트랑 합쳐서 사용

for n in x:
    print(n)
# 리스트에 있는 요소들을 하나씩 보여달라는 의미

y={"Hello","there"}
for c in y:
    print(c)

#element 위치 찾기
x=[4,2,3,1]
y=["Hello","there"]
print(x.index(3))
print(y.index("Hello"))
print("Hello"in y)

if "Hello" in y:
    print("Yes there is.")
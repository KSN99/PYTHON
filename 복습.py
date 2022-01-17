fruit = ["Apple","Apple","Banana","Banana","Strawberry","Kiwi","Peach","Peach","Peach"]

d= {}
# d={} ㅡ> d={"Apple":1} ... 
for f in fruit:
# f="Apple"
    if f in d : #Apple 이라는 key가 d라는 딕셔너리에 들어있어?
        d[f] = d[f ]+1
    #사과 갯수를 하나 올려줘
    else: 
        d[f] =1 
#만약 사과 라는 밸류가 있으면, 딕셔너리에 넣고 밸류는 1로 만들어줘.

print(d)
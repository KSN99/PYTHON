# Quiz ) 파이썬 코딩 대회 주최 . 
# 댓글 이벤트 진행 
# 댓글 작성자 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 얻게 됩니다. 
# 추첨 프로그램을 작성하시오. 

#condition1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정. 
#condition2: 댓글 내용과 상관없이 무작위로 추첨하되 중복불가 . 
#condition3: random 모듈의 shuffle 과 sample 을 활용 

# <출력 예제>
# -- 당첨자 발표 -- 
# 치킨 당첨자: 1
# 커피 당첨자: [2,3,4]
# -- congratulations-- 


from random import *
lst=range(1,21)   #1~20
lst =list(lst)
print(lst)
shuffle(lst)
print(lst)

winners = sample(lst,4) #4명중 한 명은 치킨 3명은 커피 .
print("--당첨자 발표--")
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("--congratualations--")
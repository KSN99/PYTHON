#반복문 

for waiting_num in [0,1,2,3,4]:
    print("대기번호:{0}".format(waiting_num))

for waiting_number in range(5):  #0 1 2 3 4 출력
    print(waiting_number)

for waiting in range(1,6): # 12345 출력
    print("대기순:{0}".format(waiting))

starbucks = ["Ironman", "Thor", "I am grute"]
for customer in starbucks:
    print("{0}, Ready.".format(customer))

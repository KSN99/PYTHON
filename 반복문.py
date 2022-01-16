#for, while 

for i in range(3):
    print(i)
    print("fds")
    #for 반복문


i=0
while i<3:
    print("YoU")
    i=i+1
    print(i)

#무한루프에서 while 보통 사용 
#break/ continue

i=0
while True:
    print("Correct")
    i=i+1

    if i>2: 
        break


for i in range(100):
    print(i)
    print("Stop")
    if i>2:
        break


for i in range(3):
    print(i) 
    print("continue")
    print("continue2")

    if i ==1:
        continue #특이한 조건에서 밑에 코드를 재생시키고 싶지않을 때

    print("continue3")
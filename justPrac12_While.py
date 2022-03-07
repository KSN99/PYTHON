#while

customer = "Thor"
index = 5

while index>=1:
    print("{0}, coffee is ready. {1} remains".format(customer, index))
    index-=1
    if index ==0:
        print("Coffee has been thrown.")



customer1= "Ironman"
index1 = 1
while index1==1:
    print("{0}, coffee is ready. {1}".format(customer1,index1))
    index1 +=1


####################

customer3="KIM"
person="Unkwon"

while person != customer3:
    print("{0}, coffee is ready.".format(customer3))
    person = input("What is your name sir? : ")

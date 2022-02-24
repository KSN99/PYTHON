#문자열 포맷
print("I am {}".format(24))
print("i like {} and {}".format("red","blue"))
print("i like {1} and {0}".format("red","blue"))

#방법 2 

print("I am {age},  i like {color}".format(age=20,color="blue"))

#방법 3 

age = 24
color = "blue"
print(f" am {age},  i like {color}")

#탈출 문자 

print("백문이 불여일견\n")
print("I am \"kim\"")

# \"  \'

#\\ : \ 츨력 
print("c:\\user")

# \r : 커서를 맨 앞으로 이동 
print("Red Apple\r pine")

# \b 백스페이스 역할 
print("Redd\bApple")

#\t : 탭
print("Red\tApple")

site = "http://naver.com"
password = site[7:12]

key= password[0:3]+str(len(password))+str(password.count("e"))+"!"
print("{0} password: {1}".format(site,key))
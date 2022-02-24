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
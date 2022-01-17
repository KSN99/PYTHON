# x= list()#elements 들을 그룹핑 할 때 사용 
# y= []

# print(x)
# print(y)


x= [1,2,3,4]
y= ["hi","hello"]
z= [ "hi",1,2,3]
print(x)
print(y)
print(z)
print(x+y)
print(x[0])

x[3]=10 #리스트안에 있는 요소 변경가능!
print(x)

num_elements = len(x)
print(num_elements)
#############################
a= [3,4,2,1] # sort function

b = sorted(a)
print(b)
c= sum(a)
print(c)
# 집합 (set)
# 중복 x 순서 없음 

my_set = {1,2,3,3,3}
print(my_set)

java = {"Y","K","P"}
python =set(["Y","O"])

#교집합 (자바와 파이썬 모두 가능한 사람)

print(java & python)
print(java.intersection(python))

#합집합

print(java | python)
print(java.union(python))
#순서 보장 x 

#차집합 (java 0 python x )
print(java-python)
print(java.difference(python))

# 파이썬 할 줄 아는 사람이 늘어남 
python.add("K")
print(python)

#java 를 까먹음
java.remove("K")
print(java)
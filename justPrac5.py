cabinet = {3:"Y", 100:"K"}  # key / value 
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) #프로그램 종료
print(cabinet.get(5)) # none 출력 
print(cabinet.get(5,"Usable"))

print(3 in cabinet)
print(5 in cabinet)
print(cabinet)

cabinet2 = {"A-3":"L","B-100":"T"} # key  값에 str 값 사용 가능.  
print(cabinet2["A-3"])
print(cabinet2["B-100"])

#새 손님
print(cabinet2)
cabinet2["A-3"] = "kuk"
cabinet2["C-20"]="J"
print(cabinet2)

# 간 손님
del cabinet2["A-3"]
print(cabinet2)

# key 들만 출력 
print(cabinet2.keys())
#values 만 출력
print(cabinet2.values())

print(cabinet2.items())

# 폐점 
cabinet.clear()
cabinet2. clear()
print(cabinet)
print(cabinet2)
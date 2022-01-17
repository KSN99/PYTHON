# key & value 로 이루어진 자료구조

# x=dict{}
# y={}
# print(x)

x={
    "name": "KIM",
    "age":20,
}

print(x)
print(x["name"])
print(x["age"]) 
# key 값은 불변하는 값들만 가능. ex/string int

x={
    0:"K",
    1:"L",
    "age":24,
}

print(x[0])
print(x["age"])
print("age" in x)

print(x.keys())
print(x.values())

for key in x:
    print(key)
    print(x[key])
    print("key:" + str(key))
    print("value:"+ str(x[key]))

    x[0] = "킴"
    print(x)

    #새로운 키 값에 새로운 밸류 넣기

x={
    0:"K",
    1:"L",
    "age":24,
}
x["school"] = "한빛"
print(x)
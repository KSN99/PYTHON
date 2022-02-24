subway = [1,2,3 ]
print(subway.index(1))
subway.append(4)
print(subway)

#5를 1과 2 사이에 넣기
subway.insert(1,5)
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) #맨뒤에 한명 뺴고 나머지 출력. 
print(subway)

print(subway.pop())

subway.append(5)
print(subway)
print(subway.count(5))

#정렬도 가능
num_list =[7,3,1,4]
num_list.sort()
print(num_list)

#순서 뒤집기 
num_list.reverse()
print(num_list)

#모두지우기
num_list.clear()
print(num_list)
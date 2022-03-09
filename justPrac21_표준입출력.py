print("Python","Java","javascript",sep=" , ",end=" ? ")  #end ㅡㅡ> 문장의 끝 부분을 "?"로 바꿔달라는 의미. 
print("Which language is the best?")


import sys
print("Python", "Java", file=sys.stdout) #표준 출력어로 문자 출력
print("Python", "Java", file=sys.stderr) #표준 에러로 문자 출력 


scores = { "math":0, "Eng":50, "coding":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4), sep=" : ")   # ljust ㅡㅡ> 왼쪽으로 8칸 정렬. 



#은행 대기 순번 표 
# 001 002 003 004 .. .
for num in range(1,21):
    print("대기번호:"+str(num).zfill(3))  #zfill >> 0을 채움 . 숫자는 3개만큼의 칸을 의미 . 


answer = input("Put any value:") # 사용자 입력을 통해서 값을 받게되면 항상 문자열 형태로 저장.
print(type(answer))
print("The value is " + answer+"..")
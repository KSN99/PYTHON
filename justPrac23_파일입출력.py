# score_file = open("score.txt", "w", encoding="utf8")
# print("Math:0", file=score_file)
# print("Eng: 50",file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding="utf8") # a append 파일내용에 덮어쓰기
# score_file.write("Science : 80")
# score_file.write("\nCoding: 100")
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="")  # 줄별로 읽기 , 한 줄 읽은 뒤 커서는 다음줄로 이동. 
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break 
#     print(line, end="")
# score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()#list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
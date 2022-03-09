import pickle
# profile_file = open("Profile.pickle", "wb")    w -write b- binary (pickle 사용하기위해서 )
# profile = {"Name": "park", "age":30, "hobby":["soccer","golf","coding"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile 에 있는 정보를 file 에 저장. 
# profile_file.close()

profile_file = open("Profile.pickle", "rb")   # w -write b- binary (pickle 사용하기위해서 )
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기 . 
print(profile)
profile_file.close()

# 우리가 가지고 있는 데이터를 피클을 이용해서 어떠한 파일의 저장을 해서 파일에 있는 내용을
#로드를 통해서 불러와서 사용 가능하게 하는 라이브러리. 
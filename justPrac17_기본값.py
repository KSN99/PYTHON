def profile(name, age, main_language):
    print("Name: {0}\t AGe: {1}\t Main Language: {2}"\
        .format(name,age,main_language))


profile("유재석",20,"파이썬")
profile("KIM",25,"JAVA")

# 같은 학교, 같은 학년, 같은 반, 같은 수업

def profile2(name1, age1=17,main_language1="Python"):
    print("이름:{0} 나이:{1} 주 사용 언어: {3}".format(name1,age1,main_language1))

profile2("김성년")
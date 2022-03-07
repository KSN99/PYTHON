def profile(name,age,main_lang):
    print(name, age, main_lang)

profile(name="KIm", main_lang="Java", age=32)


#가변 인자 

#def cv(name,age, lang1, lang2, lang3,lang4,lang5):
#    print("이름:{0}\t Age:{1}\t".format(name,age),end= " ")
#    print(lang1,lang2,lang3,lang4,lang5)

def cv(name,age,*language):
    print("이름:{0}\t Age:{1}\t".format(name,age),end= " ")
    for lang in language:
        print(lang,end=" ")
    print()
cv("YU",20,"Py","c","java","c#","Kotlin","HTML")
cv("KIM",25,"Swift","Ruby")
# continue
# break 

absent = [2,5]
no_book = [7]

for student in range(1,11):
    if student in absent:
        continue # 스킵하는 역할?
    elif student in no_book:
        print("Get out. {0}".format(no_book))
        break 
    print({"{0}, Hello".format(student)})
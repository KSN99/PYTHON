try:
    print("나누기 전용 계산기")
    nums = []

    nums.append(int(input("첫번째 숫자를 입력하세요:")))
    nums.append(int(input("첫번째 숫자를 입력하세요:")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} /{1} = {2}".format(nums[0],nums[1], nums[2]))
except ValueError:
    print("Error! Wrong value.")

except ZeroDivisionError as err:
    print(err)

except:
    print("Error")
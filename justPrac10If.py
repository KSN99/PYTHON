weather = input("How is today's weather?: ")
if weather == "rain" or weather =="snow":
    print("bring umbrella")
elif weather =="미세먼지":
    print("bring mask")
else:
    print("Don't have to bring anything.")


temp = int(input("기온은 어떤가요?"))
if 30<= temp:
    print("Too hot")

elif 10 <=temp and temp <30:
    print("Weather is good ")

elif 0<= temp and temp <10:
    print("Bring ur clothes")
else: 
    print("Too cold.")

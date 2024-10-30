score = int(input("กรุณาใส่คะแนน: "))
if score > 100:
    print("error")
elif score >= 80:
    print("4")
elif score >= 70:
    print("3")
elif score >= 60:
    print("2")
elif score >= 50:
    print("1")
elif score < 0:
    print("error")
else:
    print("0")
    print("คุณสอบตก ")
    print("คุณต้องการแก้ 0 ไหม")
solve = int(input("ถ้าใช่กด y ถ้าไม่กด  n \n คำตอบคือ : " ))
if solve == 1:
        print("คุณขาดคะแนนอีก "+str(50-score)+"  ถึงจะสอบผ่าน")
elif solve == 2:
        print("มึงมันโง่จริงๆๆ")
else :
    print("กรอกตัวเลขใหม่อีกครั้ง")

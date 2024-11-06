import random
win = 0
loss = 0
always = 0
while True:
    value1 = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(value1)
    value2 = str(input("คุณเลือก : "))
    if value2 == value1:
        print("เสมอ")
        always +=1
        print("-------------------------------------------------")
    elif(value2 =="ค้อน" and  value1 == "กรรไกร"):
        print("ชนะ")
        win +=1
        print("-------------------------------------------------")
    elif(value2 =="กรรไกร" and  value1 == "กระดาษ"):
        print("ชนะ")
        win +=1
        print("-------------------------------------------------")
    elif(value2 =="กระดาษ" and  value1 == "ค้อน"):
        print("ชนะ")
        win +=1
        print("-------------------------------------------------")
    elif value2 == "ออกเกม":
        break
    else:
        print("แพ้")
        loss +=1
        print("-------------------------------------------------")
print(f"คุณชนะทั่งหมด  {win} รอบ")
print(f"คุณแพ้ทั่งหมด  {loss} รอบ")
print(f"คุณเสมอทั่งหมด  {always} รอบ")
print(f"รวมทั่งหมด  {always+loss+win} รอบ")
print("-------------------------------------------------")
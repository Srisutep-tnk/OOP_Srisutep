resume = {"name":"" ,"no":int , "hobby":"" , "color":""}
value = int(input('จำนวนคนที่ต้องป้อน :'))
for i in range(1,value+1):
    print(f"กรุณากรอกคนที่ {i}")
    name = str(input("กรุณากรอกชื่อเล่น :"))
    resume  ["name"] = name
    no = int(input("กรุณากรอกเลขที่ :"))
    resume  ["no"] = no
    hobby = str(input("กรุณากรอกงานอดิเรก :"))
    resume  ["hobby"] = hobby
    color = str(input("กรุณากรอกสี :"))
    resume  ["color"] = color
    print(value)
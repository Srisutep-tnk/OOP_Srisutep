name = input("ชื่อ: ")
age = int(input("อายุ: "))
no = int(input("รหัสประจำตัว: "))
level = int(input("ระดับชั้น: "))
nickname = input("ชื่อเล่น: ")
height = float(input("ส่วนสูง: "))
weight = float(input("น้ำหนัก: "))
print(f"ชื่อ: {name}, อายุ: {age} ปี")
print(f"รหัสประจำตัวนักเรียน: {no}, ระดับชั้น: {level}")
print(f"ชื่อเล่น: {nickname}")
print(f"ส่วนสูง: {height} เซนติเมตร, น้ำหนัก: {weight} กิโลกรัม")

num = height + weight
print("ส่วนสูง + น้ำหนัก =",(num))
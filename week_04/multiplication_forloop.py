#สร้างโปรแกรมสูตรคูณแบบรับค่า คูณจาก 1 ไป 24 แสดงผลเฉพาะผลลัพธ์ที่หารด้วย 2 แล้วเป็นเลชคี่
value = int(input("ใส่เลขสูตรคูณ: "))
for i in range(1,25,1):
    x = i*value
    if value /2 %2 != 0:
        print(f"{value} x {i} = {x}")
value = []
num = int(input('ต้องการป้อนตัวเลขทั่งหมดกี่ตัว :'))
for i in range(1,num+1):
    num1 = int(input(f'ใส่ตัวเลขที่ {i} :'))
    value.append(num1)
print(f"ค่าเฉลี่ยทั่งหมด {value} = {sum(value)/len(value)}")
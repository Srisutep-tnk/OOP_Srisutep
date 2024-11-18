#mony.append(20) คำสั่งเพิ่ม
#money.insert(1,50) คำสั่งแทรก
#money.remove(50) ตำสั่งลบ //ต่องใส่ค่าที่จะลบ
#del money[1:3] คำสั่งลบ
#money.pop(1) ลบ 
#print(sum(money))
#print(max(money))
#print(min(money))
#print(len(money))
money = []
while True:
    num = int(input('หยอดเหรียญใส่กระปุก :'))
    money.append(num)
    print(money)
    if num == 0:
        print(f"เงินเก็บทั้งหมด = {sum(money)}")
        break
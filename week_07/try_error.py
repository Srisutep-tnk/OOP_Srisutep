try:
    price = int(input("ใส่ยอดซือ้ :"))
    if price == 0:
        raise ZeroDivisionError()
    if price < 0:
        raise Exception()
    elif price >= 5000:
        print(f"ได้รับส่วนลด 20% = {price-price*0.2}")
    elif price >= 2000 and price <= 4990:
        print((f"ได้รับส่วนลด 10% = {price-price*0.1}"))
    else:
        print("คุณไม่ได้ส่วนลด")
except ValueError:
    print("ใส่เแพาะตัวเลข")
except ZeroDivisionError:
    print("ห้ามใส่ 0")
except:
    print("ห้ามใส่ค่าติดลบ")
sum = 0
while True:
    try:    
        price = str(input("ราคาสินค้า (พิมพ์ 'exit' เพื่อออก): "))
        if price =="exit":
            print(f"ยอดรวมปัจจุบัน:{sum}")
            break
        elif int (price) == 0:
            raise ZeroDivisionError()
        elif int (price) <= 0:
            raise Exception()
        else:
            sum += int (price) 
            print(sum)
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั่น")
    except ZeroDivisionError:
        print("ราคาสินค้ามากกว่า 0")
    except:
        print("ราคาสินค้าต้องไม่ติดลบ")
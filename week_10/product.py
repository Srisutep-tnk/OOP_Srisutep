class Product:
    def __init__(self, name, stock):
        self.name = name
        self.price = []
        self.__stock = stock
    def add(self, instock):
        self.__stock += instock
    def dis(self, instock):
        self.__stock -= instock
    def edit(self):
        inprice = int(input('กรอกราคาสินค้า: '))
        self.price.append(inprice)
    def detail(self):
        return f'(มีราคา {self.price} บาท จำนวน {self.__stock} ชิ้น)'

st1 = Product('Game', 0)

while True:
    choice = input('กรุณาเลือกฟังก์ชัน: ต้องการเพิ่มพิมพ์ว่า add ถ้าจะลดจำนวนให้พิมพ์ dis ถ้าจะเช็ครายการสินค้าให้พิมพ์ check ถ้าต้องการแก้ไขราคาพิมพ์ว่า edit ออกพิมพ์ว่า exit: ')
    if choice == 'add':
        instock = int(input('ใส่จำนวนที่ต้องการเพิ่ม: '))
        st1.add(instock)
    elif choice == 'dis':
        instock = int(input('ใส่จำนวนที่ต้องการลด: '))
        st1.dis(instock)
    elif choice == 'check':
        print(f'รายการสินค้า {st1.name} มีรายละเอียดดังนี้ {st1.detail()}')
    elif choice == 'edit':
        st1.edit()
    elif choice == 'exit':
        break
print(f'รายการสินค้า {st1.name} มีรายละเอียดดังนี้ {st1.detail()}')
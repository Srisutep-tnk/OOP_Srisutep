class Library:
    def __init__(self):
        self.namebook = []

    def add_book(self):
        while True:
            choiec = input("พิมพ์ add เพื่อเพิ่ม พิมพ์ exit เพื่อออก  :")
            if choiec == 'add':
                    namebook = {}
                    namebook["namebook"] = str(input('ใส่ชื่อหนังสือ : '))
                    namebook["name"] = str(input('ใส่ชื่อผู้แต่งหนังสือ : '))
                    namebook["page"] = str(input('ใส่จำนวนหน้า : '))
                    namebook["price"] = str(input('ใส่ราคา : '))
                    self.namebook.append(namebook)
            elif choiec == 'exit':
                 break
    def show_books(self):
        print("รายชื่อหนังสือในห้องสมุด:")
        for book in self.namebook:
            print(book)
    def find_book(self):
        bookname = str(input('ค้นหาชื่อ:'))
        for i in self.namebook:
            if bookname == i['namebook']:
                print(i)
lib1 = Library()
lib1.add_book()
lib1.show_books()
lib1.find_book()
class Library:
    def __init__(self):
        self.namebook = []
    def add_book(self):
        while True:
            choiec = input("พิมพ์ add เพื่อเพิ่ม พิมพ์ exit เพื่อออก  :")
            if choiec == 'add':
                     bookname = str(input('ใส่ชื่อหนังสือ : '))
                     self.namebook.append(bookname)
            elif choiec == 'exit':
                 break
    def show_books(self):
        print("รายชื่อหนังสือในห้องสมุด:")
        for show_book in self.namebook:
            print(show_book)
    def find_book(self):
        bookname = str(input('ใส่ชื่อ:'))
        i = 0
        for i in self.namebook:
            if bookname == i:
                print(i)
lib1 = Library()
lib1.add_book()
lib1.show_books()
lib1.find_book()
print(lib1.namebook)
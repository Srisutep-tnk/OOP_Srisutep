class Cat:
    def __init__(self,ชื่อ,อายุ,เพศ,สี):  # แก้ __int__ เป็น __init__
        self.name = ชื่อ
        self.age = อายุ
        self.gender = เพศ
        self.color = สี

    def old(self):
        self.age += 1

cat1 = Cat(ชื่อ="พรีม",อายุ=19,เพศ="ตัวผู้",สี="เทา")
cat2 = Cat("ศรีเงิน", 5, "ตัวผู้", "ทอง")
cat2.old()
print(cat2.age)
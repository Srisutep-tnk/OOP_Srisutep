import random
class Student:
    def __init__(self, ชื่อนามสกุล, ชื่อเล่น, คะแนนสอบ):
        self.name = ชื่อนามสกุล
        self.nickname = ชื่อเล่น
        self.score = คะแนนสอบ
    def grade(self):
        if self.score >= 5:
            print("สอบผ่าน")
        elif self.score < 5:
            print("สอบตก")
        else:
            print("Eror")
    def random_score(self, random):
        self.score = random.randint(1, 10)

std5 = Student("ศรีสุเทพ หนูทอง", "ออมสิน", 0)
std1 = Student("เจษฏาพร สุทธิวัฒนกำจร", "เพ้นซ์", 0)
std2 = Student("พีระภัทร พุทธสาโร", "พีม", 0)
std3 = Student("ภูนิวัช วงศ์ไพบูลย์กุล", "โชกุน", 0)
std4 = Student("สรพัศ ทองเผือก", "ภูมิ", 0)

std = [std1, std2, std3, std4, std5]
for student in std:
    student.random_score(random)
    print(f"ชื่อ-นามสกุล : {student.name}")
    print(f"ชื่อเล่น : {student.nickname}")
    print(f"คะแนนสอบ : {student.score}")
    print("____________________________________________________________________________________________")
    student.grade()
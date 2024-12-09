class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
        self.grade = {}
    def score(self):
        choice = input("กรุณาเลือกวิชาที่จะกรอรคะแนน \n มีวิชาดังนี้ M T S :")
        score = int(input("ใส่คะแนน :"))
        grade = self.grader(score)
        if choice == "M":
            self.grade["Mat"] = grade
        elif choice == "T":
            self.grade["Thai"] = grade
        elif choice == "S":
            self.grade["Scl"] = grade
    def grader(self,score):
        if score >= 80:
            return 4
        elif score >= 70:
            return 3
        elif score >= 60:
            return 2
        elif score >= 50:
            return 1
        else:
            return 0

stu1 = Student("aomm",67319010019,19)
stu1.score()
print(stu1.grade)
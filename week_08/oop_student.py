class Student:
    def __init__(self,student_name,student_id,student_age,student_grades):
        self.name = student_name
        self.id = student_id
        self.age = student_age
        self.grades = student_grades
    def modify(self):
        self.grades["Match"] = int(input("ใส่เกรดคณิต: "))
        self.grades["Thai"] = int(input("ใส่เกรดไทย: "))
        self.grades["Eng"] = int(input("ใส่เกรดอังกิด: "))
        self.grades["sci"] = int(input("ใส่เกรดวิทย์: "))
        self.grades["social"] = int(input("ใส่เกรดสังคม: "))
    def avg_grades(self):
        return sum(self.grades.values()) / len(self.grades)

std1 = Student("xxx",67319010019, 19,{})
std1.modify()
average = std1.avg_grades()
print(f"ชื่อ {std1.name} รหัสนักเรียน {std1.id} อายุ {std1.age} เกรด {std1.grades} ได้เกลดเฉลี่ย {average:.2f}")
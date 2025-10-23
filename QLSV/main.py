# Minh họa Python OOP

# Định nghĩa lớp sinh viên
class Student:
    # Thuộc tính tĩnh chứa tổng số sinh viên được tạo ra
    totalCount = 0
    # Phương thức khởi tạo
    def __init__(self,id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
        Student.totalCount += 1
    # Phương thức in thông tin sinh viên
    def DisplayInfo(self):
        print("Student ID:",self.id)
        print("Student Name:",self.name)
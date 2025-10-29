# # Minh họa Python OOP
#
# # Định nghĩa lớp sinh viên
# class Student:
#     # Thuộc tính tĩnh chứa tổng số sinh viên được tạo ra
#     totalCount = 0
#     # protected member
#     _uniname = "Nha Trang University"
#     # private member
#     __deptName = "CNTT"
#     # Phương thức khởi tạo
#     def __init__(self,id, name, grade):
#         self.id = id
#         self.name = name
#         self.grade = grade
#         Student.totalCount += 1
#     # Phương thức in thông tin sinh viên
#     def DisplayInfo(self):
#         print("Student ID:",self.id)
#         print("Student Name:",self.name)
#         print("Student Grade:",self.grade)
#         # Nạp chồng phương thức
#     @property
#     def ToString(self):
#         return (f"{self.id}\t{self.name}\t{self.grade}")
# # Chương trình chính
# if __name__ == "__main__":
#     # Khởi tạo đối tượng sinh viên
#     student = Student(1,"John","A")
#     # student.DisplayInfo()
#     # Khi property thì ToString bỏ dấu đóng ngoặc
#     print(student.ToString)
#     # Tạo đối tượng sinh viên 2
#     student2 = Student(2,"Alan","B")
#     print(student2.ToString)
#     print(f"Student Total: {Student.totalCount}")
#
#     # Create a list of students
#     studentList = [student,student2]
#     for student in studentList:
#         print(student.ToString)
#     print(Student._uniname)
#     print(student._Student__deptName)



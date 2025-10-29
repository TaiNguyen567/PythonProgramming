# # Tạo, xử lý danh sách các đối tượng
# # Các phần tử trong danh sách không bắt buộc cùng kiểu
# my_list = [1,2,3,4,5]
# print(my_list)
# # Tạo danh sách sử dụng cú pháp list comprehension
# squares =[x**2 for x in range(1,6)]
# print(squares)
# #Tạo danh sách có các phần tử không cùng kiểu
# dssv = ['Nguyễn Hoàng Lưu',7.5]


## Các xử lý với kiểu danh sách
# duyệt các phần tử
#Cách 1:
# my_list =[1,2,3,4,5]
# for element in my_list:
#     print(element,end="")
# #Cah 2: tuy xuat thong tin qua chi so
# print("\n")
# for i in range(len(my_list)):
#     print(my_list[i],end="")
#
# #Them phan tu vao danh sach
# my_list = [1,2,3,4,5]
# my_list.append(4)
# print(my_list)
# #Xoa phan tu khoi danh sach
# my_list = [1,2,3,4,5]
# del my_list[2]
# print(my_list)

#Sap xep danh sasch
# my_list = [1,2,3,4,5,1,2,5,7,9,3,1]
# my_list.sort(reverse=True)
# print(my_list)

# #Truy xuất danh sách con
# my_list = list(range(20))
# # Tao danh sach con gom cac phan tu co chi so trong doan [1:3]
# sub_list= my_list[1:4]
# print(sub_list)

# #Tạo danh sách gôm n phần tử đầu tiên
# n=5
# first_n_elements = my_list[:n]
# print(first_n_elements)
# #Tạo danh sách gồm n phần tử cuối cùng
# last_n_elements = my_list[-n:]
# print(last_n_elements)

## Kiểu dữ liệu từ điển(Dictionary)
# Tạo một biến kiểu từ điển chứa thông tin của một sinh viên
# student_info={
#     "MSSV":"65131861",
#     "Name":"Nguyễn Hoàng Lưu",
#     "DiemTB": 7.5
#     }
# print(student_info)
# print(student_info["MSSV"])
# print(student_info["Name"])
# print(student_info["DiemTB"])
#
# #Tạo một từ điển sử dụng constructor
# student_info=dict()
# student_info["MSSV"]="65131861"
# print(student_info)

#Cho đoạn văn bản sau
#Đếm số lần xuất hiện của từng từ
#Tìm từ xuất hiện nhiều nhất
st="""Hôm qua, bốn tỉnh trọng điểm mưa lũ sau bão Matmo gồm Thái Nguyên, Cao Bằng, Bắc Ninh, Lạng Sơn hầu như không mưa, trời nắng. Lũ các sông tiếp tục lên, hoặc đang ở mức cao do mưa lớn hai ngày trước đó. Mưa lũ đã làm 8 người chết và 5 người mất tích, 7 người bị thương. Gần 17.000 ngôi nhà bị ngập, trong đó Thái Nguyên gần 5.100, Cao Bằng gần 7.300; Lạng Sơn 3.000...; 1.600 nhà bị cô lập chủ yếu ở Lạng Sơn và Thái Nguyên."""
#Tách văn bản thành các từ vào danh sách
words=st.split()
# print(words)
#Tạo từ điểm chứa số lần xuất hiện cảu mỗi từ
word_count={} #Khởi tạo từ đieern rỗng
# Xét từng từ trong danh sách
for w in words:
#Kiểm tra nếu từ chưa xuất hiện trong từ điển
#Bổ sung vô từ điểm & khởi tạo giá trị =1
    if w not in word_count:
        word_count[w]=1

    #Ngược lại nếu từ đã có trong từ điển thì chỉ cần tăng số lượng lên 1 (+1)
    else:
        word_count[w]+=1
# for k,v in word_count.items():
#     print(k,":",v)

sorted_word = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for st,word_count in sorted_word:
    print(st,":",word_count)

# ds_so_chan = list(filter(lambda n : n%2== 0,range(2,10)))
# print(ds_so_chan)
import math

from sqlalchemy import false


# Lọc số lẻ
# ds_so_le = list(filter(lambda x:x%2!=0,range(1,20)))
# print(ds_so_le)

# Lọc từ bắt đầu bằng chữ "a"
# tu_vung = ['apple', 'banana', 'avocado', 'cherry', 'apricot', 'blueberry']
# ds_tu_a = list(filter(lambda x : x[0] =='a', tu_vung))
# print(ds_tu_a)

# Lọc số nguyên tố nhỏ hơn 50
# def is_snt(a):
#     if a<0:
#         return False
#     if a==2:
#         return True
#     if a%2==0:
#         return False
#     gioi_han = int(math.sqrt(a))
#     for i in range(3,gioi_han,2):
#         if a%i==0:
#             return False
#
#     return True
# ds_snt_50 = list(filter(is_snt, range(1,50)))
# print(ds_snt_50)
# primesNums = [i for i in range(100) if isPrime(i)]
# print(primeNums)


# lọc sinh viên đậu
# sinh_vien = [
#     {'ten': 'An', 'diem': 7},
#     {'ten': 'Bình', 'diem': 4},
#     {'ten': 'Cường', 'diem': 8},
#     {'ten': 'Dũng', 'diem': 5},
#     {'ten': 'Hoa', 'diem': 9},
# ]
# ds_sv_pass = list(filter(lambda x:x['diem']>5, sinh_vien))
# for d in ds_sv_pass:
#     print(d['ten'])

# Lọc chuỗi chứa chữ số
# chuoi = ['abc', '123', 'hello', 'a1b2', 'xyz', '098']
# ket_qua = list(filter(lambda s: any(char.isdigit() for char in s), chuoi))
# print(ket_qua)


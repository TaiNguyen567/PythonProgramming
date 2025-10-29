#Tạo danh sách các số nguyên liên tiếp từ 1 đến 10
# number = [i for i in range(1, 11)]
# print(number)
#


# #Số nguyên chẵn liên tiếp từ 2 đến 100
# even_nums1 = [i for i in range(2, 100, 2)]
# print(even_nums1)
# #or
# even_nums2 = [i for i in range(2, 100, 2) if i % 2 == 0]
# print(even_nums2)


# def IsPrime(n):
#     if n < 2:
#         return False
#     for i in range (2,n//2+1):
#         if n%i==0:
#             return False
#     return True
# prime_nums = [ i for i in range(100) if IsPrime(i) ]
# print(prime_nums)


#Cach 1
# n=5
# for i in range(n):
#     for j in range(i):
#         print("*" ,end=" ")
#     print("*" )

#cach 2 (pythonic way)
# n=5
# for i in range (n+1):
#     print("*" *i)

#Dang 2
n=3
for i in range(n+1):
    print(" "*(n-i), end="")
    print("*" *i)

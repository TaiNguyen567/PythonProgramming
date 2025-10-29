# Nhập 1 năm dương lịch, kiểm tra năm đó có phải năm nhuận
# Biết năm nhuận là năm dương lịch thỏa 1 trong 2 điều kiện
# Chia hết 400 hoặc
# Chia hết cho 4 và không chia hết cho 100

#Nhập dữ liệu

while True:
    try:
        year = int(input("Nhap nam duong lich : "))
    except :
        print("Nam khong hop le!!!!")
    else:
        if year>0:
            break
        else:
            print("Nam phai lon hong 0!!!")

#Kiểm tra năm nhuận

if year % 400==0 or (year%4==0) and (year%100!=0) :
    print("Nam nhuan")
else :
    print("Nam khong nhuan")

#Xep loai hoc tap dua tren diem trung binh

dtb = float(input("Nhap diem trung binh : "))

if dtb>=9:
    print("Xuat sac")
elif dtb >=8:
    print("gioi")
elif dtb >=7:
    print("kha")
elif dtb>=5:
    print("Trung binh")
else:
    print("Yeu")
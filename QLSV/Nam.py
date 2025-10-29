nam=int(input())
dia_chi=["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]
thien_can=["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","QUý"]

dia=dia_chi[(nam+8)%12]
thien=thien_can[(nam+6)%10]
print(f"{dia} {thien}")
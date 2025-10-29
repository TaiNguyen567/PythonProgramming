while True:
    try:
        n=int(input("Nhap  5<=n<=100: "))
    except :
        print("gia tri ko hop le")
    else:
        if 5<=n<=100 :
            break
        else:
            print("n khong thoa man")

print("n=%d" %n)



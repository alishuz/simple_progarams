while True:
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    amal = input("Amalni kiriting, chiqish=0: ")
    if amal == "/":
        c = a / b
    elif amal == "*":
        c = a * b
    elif amal == "-":
        c = a - b
    elif amal == "+":
        c = a + b
    if amal == "0":
        break
    javobt = input(f"Misolning javobi {c} ga teng, to'g'rimi chiqish=0~~~")
    if javobt == "0":
        break
    if javobt == "ha":
        print("Yaxshi fikringiz uchun rahmat, HURMATLI FOYDALANUVCHI!!!")
    elif javobt == "yo'q":
        print("Yomon fikringiz uchun ham rahmat, HURMATLI FOYDALANUVCHI!!!")
    if javobt == "0":
        break
print("DASTUR TUGADI!!!")
print(" Foydalanganingiz uchun, RAHMAT!!!")

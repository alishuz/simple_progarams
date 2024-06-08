while True:
    yosh = int(input("Yoshingiz nechchida: "))
    if yosh == 0:
        break
    if yosh >= 1 and yosh < 6:
        b = input("Siz bog'chaga borar ekansiz, chiqish=0>>>")
    elif yosh <= 18:
        b = input("Siz maktabga borar ekansiz, chiqish=0>>>")
    elif yosh <= 50:
        b = input("Siz ishga borar ekansiz, chiqish=0>>>")
    elif yosh >= 50:
        b = input("Siz nafaqada ekansiz, chiqish=0>>>")
    if b == "0":
        break
print("DASTUR TUGADI!!!")
print(" Foydalanganingiz uchun, RAHMAT!!!")
    
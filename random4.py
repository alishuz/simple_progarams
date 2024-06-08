import random as r
while True:
    a = r.randint(1,100)
    while True:
        b = int(input("Nechchini o'yladim 1dan 100gacha, chiqish=0: "))
        if b < a:
            c = a - b
            print(f"{c} ni qo'shing {b} ga.")
        elif b > a:
            c = b - a
            print(f"{c} ni ayiring {b} dan.")
        elif b == a or a == b:
            you = input("To'g'ri topdingiz!!!, ortga=0>>>")
        elif you == "0":
            break    
print("DASTUR TUGADI!!!")
print(" Foydalanganingiz uchun, RAHMAT!!!")
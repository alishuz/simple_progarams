import random as r
print("TOSH QAYCHI VA QOG'OZ O'YINIGA HUSH KELIBSIZ!!!")
tanlovlar = ["tosh", "qaychi", "qog'oz"]
while True:
    tanlov = r.choice(tanlovlar)
    inson = input("Tanla: tosh qog'oz qaychi = ")
    if inson == "chiqish":
        break
    print(f"Siz {inson}ni tanladingaiz.")
    print(f"Kompyuter {tanlov}ni tanladi.")
    if (tanlov == "tosh" and inson == "qog'oz") or (tanlov == "qog'oz" and inson == "qaychi") or (inson == "tosh" and tanlov == "qaychi"):
        print("Siz yutdingiz!!!")
    elif (tanlov == "qog'oz" and inson == "tosh") or (tanlov == "qaychi" and inson == "qog'oz") or (inson == "qaychi" and tanlov == "tosh"):
        print("Siz yutqizdingiz~~~")
    elif (tanlov == "tosh" and inson == "tosh") or (tanlov == "qaychi" and inson == "qaychi") or (tanlov == "qog'oz" and inson == "qog'oz"):
        print("DURRANG BO'LDI!")
    else:
        print("Siz xato yozdingiz!")
print("O'YIN TUGADI!!!")
print("O'ynaganingiz uchun rahmat!!!")

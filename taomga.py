taomlar = ["manti", "kabob", "somsa", "sho'rva", "non", "choy", "lavash", "burger","gamburger","hotdog", "sendvich", "sentvich","go'sht", "shashlik","pitsa"]
while True:
    buyurtma = input("Nimani buyurtma qilasiz: ")
    if buyurtma in taomlar:
        cod = input(f"Bizda {buyurtma} bor, chiqish=0>>>")
    if buyurtma not in taomlar:
        cod2 = input(f"Bizda {buyurtma} yo'q, chiqish=0>>>")
    elif cod == "0":
        break
    if cod2 == "0":
        break
print("DASTUR TUGADI!!!")
print("Bizning dasturimizdan foydalanganingiz uchun, RAHMAT!!!")
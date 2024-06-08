a = input(">>>")
if a == "salom":
    print("Vaalaykum assalom, hurmatli foydlalanuvchi")
    b = input("Ismingiz nima?>>>")
else:
    print("Siz ma'lumotlarni noto'g'ri kiritgansiz.")
    b = input("Ismingiz nima?>>>")
if b == "Alisher":
    input("Siz shu dasturning yaratuvchisi ekansiz, to'g'rimi?>>>")
    print("ok")
elif b == "Firuza":
    input("Siz yaratuvchining onasi ekansiz, to'g'rimi?>>>")
    print("ok")
elif b == "Qaxramon":
    input("Siz yaratuvchining otasi ekansiz, to'g'rimi?>>>")
    print("ok")
elif b == "Ozodbek":
    input("Siz yaratuvchining ukasi ekansiz, to'g'rimi?>>>")
    print("ok")
else:
    input("Siz ma'lumotlarni noto'g'ri kiritgansiz, to'g'rimi?>>>")
    print("ok")
print("Men sun'iy intelektman!!!")
input("Sizning yoshingiz nechchida?>>>")
print("Yaxshi...")
c = input("Endi sen menga savol ber>>>")
c = c.lower
if c == "kimsan?":
    print("Men Alisher tomonida yaratilga sun'iy intelektman.")
elif c == "yoshing nechchida?" or "necha yoshdasan":
    print("Meni yaratilganimga ko'p vaqt bo'lmadi hali.")
elif c == "isming nima?":
    print("Mening ismim AlisherAI.")
elif c == "seni kim yaratgan?":
    print("Qahorov Alisher Qaxramonovich")
elif c == "sen nimalarni bilasan?":
    print("Meni ma'lumotlar bazam juda oz~")
elif c == "sen menga yordam bera olasanmi?":
    print("Qo'limdan kelgancha yordam beraman!")
else:
    print("Kechirasiz, bu savolingiz meni ma'lumotlar bazamda yo'q ekan~")
print("HAYR DO'STIM!!!")

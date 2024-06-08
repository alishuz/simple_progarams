import random as r
print("Bu o'yinda siz 1da 10gacha tahminiy sonni topasiz urinish 2 marta, sizga OMAD!!!")
while True:
    son = r.randint(1,10)
    oy = int(input("Men o'ylagan sonni top, 1dan 10gacha, imkon 2 marta: "))
    if son < oy:
        oy = int(input("Kichikroq sonni tanlang~ 0=tugatish>>>"))
    if son > oy:
        oy = int(input("Kattaroq sonni tanlang~ 0=tugatish>>>"))             
    if son == oy:
        oy = int(input("To'g'ri topdingiz tabriklayman!!! 0=tugatish>>>"))
    if oy == 0:
        break        
print("O'YIN TUGADI!!!") 
print("O'ynaganingiz uchun rahmat!") 
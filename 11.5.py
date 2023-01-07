mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka',
               'olma', 'banan', 'uzum', 'qovun']
savat=[]
for n in range(5):
    savat.apppend(input(f"Savatga {n+1} - mahsulot nomini kiriting:\n>>>"))
b_mahsulot=[] 
mavjud_emas=[]
for mahsulot in savat:
        if mahsulot in mahsulotlar:
            b_mahsulot.append(mahsulot)
        else:
            mavjud_emas.append(mahsulot)
if mavjud_emas:
    for mahsulot in mavjud_emas:
        print(f"Do'konimizda quyidagi {mahsulotlar} yo'q")
else:
    print("Dokonimizda siz so'ragan barcha mahsulot bor")
            
    

        
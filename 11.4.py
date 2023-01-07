# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 02:13:16 2023

@author: 9999
"""

mahsulotlar=["karam","olma","anjir","nok","kartoshka",'pampers','non','qovun','tarvuz','gilos']
savat=[]
print("5 ta mahsulot kiriting:")
for n in range(5):
    savat.append(input(f"Savatga {n+1} mahsulot nomini kiriting:\n>>>"))
if savat:
   for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot} do'konimizda bor!")
    else:print(f"{mahsulot} do'konimizda yo'q!")
else:print("Savatingiz bo'sh")


            

 
    



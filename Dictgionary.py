d={901:"Aarav",887:"Mayank",34:"Parth",354:"Raj",243:"Bhavik"}
print(d)
print(d[34])
d[34]="Dhurv" 
print(d)


for i in d:   #jeni pase banch of data hoy teni par for loop chale
    print(i," : ",d[i])

print(887 in d)  #ture

# Dictgionary function
print(d.copy) #copy kare
print(d.get(887)) #887 ni value aapse  $ dayrect key thi accsec thay che tema laibrery function use kari kariye chiye.
print(d.items())  # key and valyu nu per banavine aapse
print(d.keys())    # aakhi dictgionary ketli key che tenu list basnavi ne aapi dese
print(d.pop(887))      #pop ni ander aek argument pas karvi pdase  list ni andar argument aapvi padti nthi
print(d.popitem())  # last key ane velyu per rimov kari nakhsde
d1={88:"vihar",356:"Harshad",289:"Manish"}
d.update(d1)   # d list in ander biju  d1 list add thse
print(d)
print("DAFTAR HARGA BUAH")
print("_________________")
buah ={"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" :6500}

i = 0
for x,y in buah.items():
    i += 1
    print(i ,".", x ,"-",y)
jml = 0
while True:
    pil = input("Nama buah yang dibeli  = ")
    if(pil in buah):
        berat = float(input("Berapa Kg              = "))
        print("_____________________________")
        jml += (buah[pil]*berat)
        yesno = str(input("Beli buah yang lain (y/n) ?  ="))
        if yesno == "n":
            print("Total harga           :",jml)
            break
        elif yesno == "y":
            continue
        if yesno != "y" or "n":
            print("!!!!     PERINGATAN     !!!!")
            print("      input anda salah      ")
            print("harap ulangi dari input buah")
            print("_____________________________")
            jml -= (buah[pil]*berat)
            
    else:
        print("nama buah tidak ada")
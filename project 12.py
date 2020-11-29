print("Daftar harga buah")
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def data(abb):
    i = 0
    for x,y in abb.items():
        i += 1
        print(i ,".", x ,"-",y) 
data(buah)
("_____________________________")

list1 = ["Menu:",
"A. Tambah data buah",
"B. beli buah",
"C. Hapus data buah"]
for c in list1:
    print(c)

print("_____________________________")
pil = input("pilihan menu (A/B/C) = ")
print("_____________________________")


if pil == "A":
    name = input("Masukkan nama buah 		=  ")
    if(name not in buah):
        print("_____________________________")
    elif(name in buah):
        print("buah yang ingin ditambahkan sudah ada di dictionary")
            
    if name not in buah:
        while True:
            try :
                hrg = int(input("Masukkan harga satuan(hanya angka)=  "))
                break
            except ValueError:
                print("bukan angka")
        buah.update({name:hrg})
        print("Data buah (update):")
        data(buah)

        print("_____________________________")
        jml = 0
        jwb = str(input("ingin beli buah?? (y/n) ="))
        if jwb == "y":
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
                    print("Nama buah tidak ada di dictionary")
        elif jwb == "n":
            exit()

#bali barang
if pil == "B":
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
            print("Nama buah tidak ada di dictionary")

#hapus data
if pil == "C":
    while True:
        delet = str(input("nama buah yang ingin dihapus = "))
        if delet in buah:
            del(buah[delet])
            print("_____________________________")
            data(buah)
            exit()
        elif delet not in buah:
            print("_____________________________")
            print("buah ",delet," tidak ditemukan")

if pil != "A" or "B" or "C":
    print("input anda salah, tidak ada didalam menu")
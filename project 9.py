#tampilan awal
print("DAFTAR HARGA BUAH")
print("_________________")
buah ={"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" :6500}

i = 0
for x,y in buah.items():
    i += 1
    print(i ,".", x ,"-",y)

#input - output
print("_________________")
pil = input("Nama buah yang dibeli  = ")
if(pil in buah):
    berat = float(input("Berapa Kg              = "))
    print("_____________________________")
    print("Total harga           :",buah[pil]*berat)
else:
    print(pil, 'tidak ada dalam daftar buah')
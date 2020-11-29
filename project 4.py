list1 = ["Menu:",
"A. Tambah data sayur",
"B. Hapus data sayur",
"C. Tampilkan data sayur"]

for c in list1:
    print(c)

print("_______________________")
print("DAFTAR NAMA SAYUR")
a = ["bayam" , "kangkung", "wortel", "kangkung", "selada"]
pil = input("pilihan anda (A/B/C) = ")

print("_______________________")

if pil == "A":
    syrtmb = input("nama sayur yang ingin ditambahakan = ")
    a.append(syrtmb)
    print("perubahan data = ", a)
elif pil == "B":
    try:
        dele = input("nama sayur yang ingin dihapus = ")
        a.remove(dele)
        print("_______________________")
        print("DAFTAR NAMA SAYUR update")
        for x in a:
            print(x)
    except ValueError:
        print("data tidak ditemukan")
elif pil == "C":
    print(a)
else:
    print("menu yang anda pilih tidak ada")
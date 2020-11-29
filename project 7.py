def hargabuah(x):
    harga = list(x.values())
    harga.sort(reverse=True)
    plgmahal = harga[0]
    for buah, harga in x.items():
        if harga == plgmahal:
            return buah

buah ={"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" :6500}

print(hargabuah(buah))
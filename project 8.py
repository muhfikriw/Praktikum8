def rat(a):
    harga = list(a.values())
    jml = sum(harga)
    kali = len(harga)
    rumus = jml/kali
    print("rata-rata harga buah :",rumus)

buah ={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' :6500}
rat(buah)
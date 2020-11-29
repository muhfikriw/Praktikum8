# Program yang membaca input beberapa data 
# berupa biLangan bulat, kemudian menampilkan rata-ratanya. 
# Input diakhiri dengan memasukkan nilai 0

dataNilai = []
i = 1
while True: 
    print('Masukkan data ke-' + str(i) + ':', end='')
    x = int(input())
    if x == 0 :
        break
    else:
        dataNilai += [x]
    i  += 1

# proses perhitungan rata-rata
sum = 0
for i in range(len(dataNilai)):
    sum += dataNilai[i]

rerata = sum/len(dataNilai)

#output
print("rata ratanya :" + str(rerata))
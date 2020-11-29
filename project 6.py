#function sortStringByChar()
#mengurutkan berdasarkan jumlah variabel dalam list

myData = ['apel plotot', 'duren', 'jambu ber biji', 'nanas asam']

def sortStringByChar(data):
    data.sort(key = len, reverse = True)
    print(data)
sortStringByChar(myData)
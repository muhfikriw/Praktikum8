a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
a.insert(3,10)
print("a = ", end="")
print(a)
b.insert(2,15)
print("b = ", end="")
print(b)


#penambahan data terakhir
print("_"*35)
x = len(a)
a.insert(x,4)
print("a = ", end="")
print(a)
l = len(b)
b.insert(l,8)
print("b = ", end="")
print(b)


#sorting ascending
print("_"*35)
a.sort()
print("a = ", end="")
print(a)
b.sort()
print("b = ", end="")
print(b)

#penambahan data c dan d
print("_"*35)
c = a[0:7]
print("c = ", end="")
print(c)
d = b[2:9]
print("d = ", end="")
print(d)

#list e ( c + d)
print("_"*35)
x = 0
e = []
for i in c:
    k = c[x] + d[x]
    e.append(k)
    x += 1
print("e = ", end="")
print(e)

#ubah dari list ke tuple
print("_"*35)
print("Data Tuple = ", end="")
tup = tuple(e)
print(tup)

#sum, min, max
print("_"*35)
print("MIN = ", end="")
print(min(tup))
print("MAX = ", end="")
print(max(tup))
print("JUMLAH SELURUH = ", end="")
print(sum(tup))

#GANTI LIST
#GANTI LIST
#GANTI LIST
#GANTI LIST
print("")
print("_"*35)
myString = ("python adalah bahasa pemrograman yang menyenangkan")
print("python adalah bahasa pemrograman yang menyenangkan")
print("")
print("disusun menggunakan huruf = ", end="")
wkwk = set(myString)
print(wkwk)

print("")
print("_"*35)
wkwkwk = list(wkwk)
wkwkwk.sort()
print(wkwkwk )
#awalan
print("_"*25)
list1 = []
a = int(input("berapa mahasiswa? = "))
print("_"*25)
print("*"*20)
print("input data mahasiswa")
print("*"*20)

#script
def tambahdata(s):
    i = 0
    for i in range (0,a):
        i += 1
        num = str(input("Masukan nama mahasiswa ke-"+ str(i) + " = "))
        t = 0
        for i in num :
            t += 1
        chara = num + "(" + str(t) + " karakter)"
        list1.append(chara)
    
    #output
    print("*"*20)
    print("Pendataan mahasiswa")
    print("*"*20)
    list1.sort()
    for c in list1:
        print(c)


tambahdata(list1)
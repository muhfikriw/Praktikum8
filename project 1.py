#input banayak data
list1 = []
a = int(input("berapa bilangan? = "))
i = 0

#input data
for i in range (0,a):
    i += 1
    try :
        num = int(input("Masukan bilangan ke-"+ str(i) + " = "))
        list1.append(num)
    except ValueError:
        print("bukan bilangan")

#output
list1.sort(reverse=True)
print("descending =", list1)
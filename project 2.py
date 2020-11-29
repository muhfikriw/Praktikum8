def datastat(x):
    #rata-rata dari list
    data = len(x)
    jml = sum(x)
    a = jml/data

    #nilai tertinggi dari list
    b = max(x)
    #nilai terendah dari list 
    c = min(x)
    datastat = [a,b,c]
    print(datastat)

r = {2,4,6,8}
datastat(r)
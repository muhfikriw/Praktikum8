bil = [3,4,1,6,9]
print("bil  = ", bil)
print("dikuadratkan")
print("hasil = ", end="")


def kuadrat(bil):
    bila = []
    for hasil in bil:
        bila.append(hasil ** 2)
    print(bila)

kuadrat(bil)
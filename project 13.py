nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Aku', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def nimak(a):
    mak = 0
    dic = {}
    for x in a:
        uas = x.get("uas")
        mid = x.get("mid")
        rumus = (mid + 2*uas)/3
        if(rumus>mak):
            mak = rumus
            dic["nim"] = x.get("nim")
            dic["nama"] = x.get("nama")
    print("Nilai tertinggi dimiliki oleh mahasiswa ", dic["nama"] ,"dengan NIM", dic["nim"])


nimak(nilaiMhs)



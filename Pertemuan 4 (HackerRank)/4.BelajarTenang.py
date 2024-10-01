def Jarak(dB,m):
    return round(15*10**((dB-40)/20),3)

def BelajarTenang(dB, m):
    if Jarak(dB,m) > m :
        return "Isi bensin dulu, bang"
    else:
        return (f"{Jarak(dB,m)} meter")

print(BelajarTenang(102, 20000))
def catalog(kategori,VIP):
    if kategori == "elektronik":
        if VIP == True:
            return 30
        else:
            return 10
    elif kategori == "pakaian":
        if VIP == True:
            return 20
        else:
            return 5
    elif kategori == "makanan":
        if VIP == True:
            return 15
        else:
            return 2
    else:
        return 0

def diskonHari(hari,VIP):
    if VIP == True and hari == "Jumat" or hari == "Sabtu":
        return 5
    elif hari == "Rabu":
        return 5
    elif hari == "Minggu":
        return -5
    else:
        return 0
    
def pajak(kondisi):
    if kondisi == "dalam negeri":
        return 10
    elif kondisi == "luar negeri":
        return 20
    else:
        return 0
    
def hargaDiskon1(harga, kategori, VIP):
    return harga - (harga*catalog(kategori,VIP)//100)

def hargaDiskon2(harga, hari, VIP):
    return harga*diskonHari(hari,VIP)//100

def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    return hargaDiskon1(harga,kategori,VIP) - hargaDiskon2(hargaDiskon1(harga,kategori,VIP), hari, VIP) + ((hargaDiskon1(harga,kategori,VIP) - hargaDiskon2(hargaDiskon1(harga,kategori,VIP),hari,VIP))*pajak(lokasi)//100)

print(hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin"))
print(hargaAkhir(500000, "pakaian", False, "luar negeri", "Rabu"))
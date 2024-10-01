# Nama file : 3.pembagian.py
# Deskripsi : menghitung pembagian dari x dan y secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def bagi(x,y):
    if x < y:
        return 0 #basis
    else:
        return bagi(x-y, y) + 1 #rekurens
    
# APLIKASI
print(bagi(3, 5))
print(bagi(45, 5))
print(bagi(90, 5))
print(bagi(10, 5))
print(bagi(5, 5))
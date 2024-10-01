# Nama file : 2.perkalian.py
# Deskripsi : menghitung perkalian dari x dan y secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def kali(x,y):
    if y == 0:
        return 0 #basis
    else:
        return kali(x, y-1) + x #rekurens
    
# APLIKASI
print(kali(0, 5))
print(kali(1, 5))
print(kali(2, 5))
print(kali(3, 5))
print(kali(5, 5))
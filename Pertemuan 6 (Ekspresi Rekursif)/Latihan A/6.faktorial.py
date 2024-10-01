# Nama file : 6.faktorial.py
# Deskripsi : menghitung faktorial secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def faktorial(x):
    if x == 0:
        return 1 #basis
    else:
        return x * faktorial(x-1) #rekurens
    
# APLIKASI
print(faktorial(3))
print(faktorial(1))
print(faktorial(2))
print(faktorial(5))
print(faktorial(4))
# Nama file : 1.Perkalian3.py
# Deskripsi : menghitung perkalian dengan 3 secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def perkalian3(n):
    if n == 1:
        return 3 #basis
    else:
        return perkalian3(n-1) + 3 #rekurens

# APLIKASI
print(perkalian3(1))
print(perkalian3(2))
print(perkalian3(3))
print(perkalian3(4))
print(perkalian3(5))
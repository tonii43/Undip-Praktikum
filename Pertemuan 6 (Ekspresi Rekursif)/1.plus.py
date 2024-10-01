# Nama file : 1.plus.py
# Deskripsi : menghitung penjumlahan antara x dan y secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def plus(x,y):
    if y == 0:
        return x #basis
    else:
        return 1 + plus(x, y-1) #rekurens
    
# APLIKASI
print(plus(0, 5))
print(plus(1, 5))
print(plus(2, 5))
print(plus(3, 5))
print(plus(5, 5))
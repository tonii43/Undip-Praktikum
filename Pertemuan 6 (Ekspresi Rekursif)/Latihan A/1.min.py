# Nama file : 1.min.py
# Deskripsi : menghitung pengurangan antara x dan y secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def min(x,y):
    if y == 0:
        return x #basis
    else:
        return min(x, y-1) - 1 #rekurens
    
# APLIKASI
print(min(0, 5))
print(min(1, 5))
print(min(2, 5))
print(min(3, 5))
print(min(5, 5))
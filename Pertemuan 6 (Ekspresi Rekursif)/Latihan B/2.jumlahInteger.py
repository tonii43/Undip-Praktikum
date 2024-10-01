# Nama file : 2.jumlahInteger.py
# Deskripsi : menghitung penjumlahan integer secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def jumlahInteger(n):
    if n == 1:
        return 1 #basis
    else:
        return jumlahInteger(n-1) + n #rekurens
    
# APLIKASI
print(jumlahInteger(1))
print(jumlahInteger(2))
print(jumlahInteger(3))
print(jumlahInteger(4))
print(jumlahInteger(5))
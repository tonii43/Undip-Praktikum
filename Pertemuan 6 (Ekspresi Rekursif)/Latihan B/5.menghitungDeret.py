# Nama file : 5.menghitungDeret.py
# Deskripsi : menghitung jumlah deret aritmatika dengan beda bilangan ganjil berurut secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def menghitungDeret(n):
    if n == 1:
        return 1 #basis
    else:
        return menghitungDeret(n-1) + n*n #rekurens
    
# APLIKASI
print(menghitungDeret(1))
print(menghitungDeret(2))
print(menghitungDeret(3))
print(menghitungDeret(4))
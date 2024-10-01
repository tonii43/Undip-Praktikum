# Nama file : 3.deretAritmatika.py
# Deskripsi : menghitung jumlah deret aritmatika dengan beda 3 secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def deretAritmatika(n):
    if n == 1:
        return 3 #basis
    else:
        return deretAritmatika(n-1) + 3*n #rekurens
    
# APLIKASI
print(deretAritmatika(1))
print(deretAritmatika(2))
print(deretAritmatika(3))
print(deretAritmatika(4))
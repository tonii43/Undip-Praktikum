# Nama file : 4.deretGeometri.py
# Deskripsi : menghitung jumlah deret geometri dengan rasio 3 secara rekursif.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def deretGeometri(n):
    if n == 1:
        return 1 #basis
    else:
        return deretGeometri(n-1) + 3**(n-1) #rekurens
    
# APLIKASI
print(deretGeometri(1))
print(deretGeometri(2))
print(deretGeometri(3))
print(deretGeometri(4))
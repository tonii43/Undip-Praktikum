# Nama file : 4.perpangkatan.py
# Deskripsi : menghitung perpangkatan dari x dan y secara rekursif, x adalah nilai asli, dan y adalah pangkatnya.
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def pangkat(x,y):
    if y == 0:
        return 1 #basis
    else:
        return x * pangkat(x,y-1) #rekurens
    
# APLIKASI
print(pangkat(3, 3))
print(pangkat(1, 5))
print(pangkat(2, 5))
print(pangkat(2, 3))
print(pangkat(4, 2))
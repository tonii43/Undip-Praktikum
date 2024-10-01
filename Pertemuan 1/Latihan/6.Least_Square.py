# Nama file: 6.Least_Square.py
# Pembuat: Muhammad Dimas Arya Putra
# Tanggal: 2 September 2024
# Deskripsi: mencari jarak dari dua buah pasang titik koordinat kartesian

# Definisi dan spesifikasi dari fungsi LS bernama LS(x1,y1,x2,y2) adalah:
# LS : 4 real --> real

# Definisi dan spesifikasi dari fungsi antara:
# dif2 : 2 real --> real
# FX2 : real --> real

# Realisasi
def FX2(x):
    return x*x
def dif2(x,y):
    return FX2(x - y)
def LS(x1,y1,x2,y2):
    return (dif2(y2,y1) + dif2 (x2,x1)) ** 0.5

# Aplikasi
print(LS(1,1,2,2))
print(LS(9.2,6.5,1.2,3.4))
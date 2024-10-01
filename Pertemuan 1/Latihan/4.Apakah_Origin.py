# Nama file: 4.Apakah_Origin.py
# Pembuat: Muhammad Dimas Arya Putra
# Tanggal: 2 September 2024
# Deskripsi: mengecek apakah suatu nilai mewakili titik origin (0,0)

# Definisi dan spesifikasi dari fungsi IsOrigin bernama IsOrigin(x,y) adalah:
# IsOrigin : real, real --> boolean

# Realisasi
def IsOrigin(x,y):
    return x == 0 and y == 0

# Aplikasi
print(IsOrigin(0,1))
print(IsOrigin(0,0))
print(IsOrigin(1,1))
# Nama file: 5.Apakah_Valid.py
# Pembuat: Muhammad Dimas Arya Putra
# Tanggal: 2 September 2024
# Deskripsi: mengecek apakah suatu nilai berada pada jangkuan batasan angka tertentu atau tidak

# Definisi dan spesifikasi dari fungsi IsValid bernama IsOrigin(x) adalah:
# IsOrigin : integer --> boolean

# Realisasi
def IsValid(x):
    return x < 5 or x > 500

# Aplikasi
print(IsValid(2))
print(IsValid(5))
print(IsValid(500))
print(IsValid(6000))
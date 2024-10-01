# Nama file: max3.py
# Pembuat: Muhammad Dimas Arya Putra
# Tanggal: 2 September 2024
# Deskripsi: menentukan nilai maksimum dari 3 bilangan integer

# Definisi dan spesifikasi dari fungsi max3 bernama max3(a,b,c) adalah:
# max3 : 3 integer --> integer
#   max2(a,b) menentukan nilai maksimum dari 2 bilangan integer a dan b

# Realisasi
def max2(a,b):
    return ((a+b) + abs(a-b)) // 2

def max3(a,b,c):
    return max2(max2(a,b),c)

# Aplikasi
print(max3(4,9,-10))
print(max3(100,-20,300))
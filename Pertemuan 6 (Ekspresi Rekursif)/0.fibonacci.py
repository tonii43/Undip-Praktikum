# Nama file : 0.fibonacci.py
# Deskripsi : menghitung bilangan Fibonacci ke-n secara rekursif
# Pembuat   : Muhammad Dimas Arya Putra / 24060124130062
# Tanggal   : 1 Oktober 2024

# REALISASI
def fibonacci(n):
    if n == 0:
        return 0 #basis
    elif n == 1:
        return 1 #basis
    else:
        return fibonacci(n-1) + fibonacci(n-2) #rekurens
    
# APLIKASI
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(5))
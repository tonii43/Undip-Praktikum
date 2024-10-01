# Nama file: 1.Mean_Olympique(MO).py
# Pembuat: Muhammad Dimas Arya Putra
# Tanggal: 2 September 2024
# Deskripsi: menghitung rata-rata dari dua buah bilangan integer yang bukan maksimum
#            dan bukan minimum dari 4 buah integer

# Definisi dan spesifikasi:
# MO : 4 integer --> real

# Definisi dan spesifikasi fungsi antara:
# max2 : 2 integer --> integer
# min2 : 2 integer --> integer
# max4 : 4 integer --> integer
# min4 : 4 integer --> integer

# Realisasi
def max2(a,b):
    return (a + b + abs(a-b))/2
def min2(a,b):
    return (a + b - abs(a-b))/2
def max4(i,j,k,l):
    return max2(max2(i,j),max2(k,l))
def min4(i,j,k,l):
    return min2(min2(i,k),min2(k,l))

def MO(u,v,w,x):
    return (u + v + w + x - min4(u,v,w,x) - max4(u,v,w,x))/2

# Aplikasi:
print(MO(8,12,10,20))
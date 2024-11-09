# Nama File : list_nim.py
# Deskripsi : Type dan Operasi List
# Pembuat :
# Tanggal : 28 Oktober 2024

# DEFINISI DAN SPESIFIKASI TYPE
# Konstruktor menambahkan elemen di awal, notasi prefix
# type List: [] atau [e o List]
# Konstruktor menambahkan elemen di akhir, notasi postfis
# type List: [] atau [List o e]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List -> List
# Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e,L):
    return [e] + L

# Konsi: List, elemen -> List
# Konsi(L,e) -> menghasilkan sebah list dari L dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(L,e):
    return L + [e]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong > elemen
# FirstElmt(L) Menghasilkan elemen pertama list L
# Realisasi
def FirstElmt(L):
    return L[0]

# LastElmt: List tidak kosong -> elemen
# LastElmt(L): mengembalikan elemen terakhir terakhir list L
# Realisasi
def LastElmt(L):
    return L[-1]

# Tail : List tidak kosong > List
# Tail(L) : Menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi
def Tail(L):
    return L[1:]

# Head : List tidak kosong > List
# Head(L) : Menghasilkan list tanpa elemen terakhir list L, mungkin kosong
# Realisasi
def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty : List > boolean
# IsEmpty(L) benar jika list kosong
# Realisasi
def IsEmpty(L):
    return L == []

# IsOneElmt: List + boolean
# IsOneElmt (X,L) adalah benar jika list L hanya mempunyai satu elemen
# Realisasi
def IsOneEmlt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt : List + integer
# NbElmt(L) : Menghasilkan banyaknya elemen list, nol jika kosong
# Realisasi
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else :
        return 1 + NbElmt(Tail(L))

# APLIKASI
print(Konso(2,[3]))
print(Konsi([3,4,5],6))
print(FirstElmt([3,4,5,6,7]))
print(LastElmt([3,4,5,6,7]))
print (Tail([3,4,5,6,7]))
print (Head([3,4,5,6,7]))
print(IsEmpty([]))
print(IsEmpty( [3,4, 5,6,7]))
print(IsOneEmlt([]))
print(IsOneEmlt([3]))
print(IsOneEmlt([3,4,5,6,7]))
print(NbElmt([3,4,5,6,7]))
# Nama File : treeNaire_24060124130062.py
# Pembuat   : Muhammad Dimas Arya Putra
# Tanggal   : 19 November 2024
# Deskripsi : Tree Naire atau Pohon N-ner adalah rangkaian tipe yang terdiri dari akar dan anak

from list import *

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

def makePN(A, PN):
    return [A, PN]

# DEFINISI DAN SPESIFIKASI SELEKTOR

# Akar : PohonN-ner tidak kosong -> elemen
# {Akar(P) adalah akar dari P. Jika P adalah (A, PN) = Akar(P) adalah A}
def akar(PN):
    return PN[0]

# Anak: PohonN-ner tidak kosong → list of PohonN-ner
# {Anak(P) adalah list of pphon N-ner yang merupakan anak-anak (sub pohon) dari P. Jika P adalah (A, PN) = Anak (P) adalah PN }
def anak(PN):
    return PN[1]

# DEFINISI DAN SPESIFIKASI PREDIKAT

# IsTreeNEmpty : PohonN-ner → boolean_
# {IsTreeNEmpty(PN) true jika PN kosong : ()}
def isTreeNEmpty(PN):
    return PN == []

# IsOneElmt : PohonN-ner → boolean
# {IsOneElmt(PN) true jika PN hanya terdiri dari Akar
def isOneElmt(PN):
    return (isTreeNEmpty(PN) == False) and (isTreeNEmpty(anak(PN)) == True)

# DEFINISI DAN SPESIFIKASI FUNGSI/OPERASI

# NbNELmt: PohonN-ner → integer ≥ 0
# {NbNElmt(PN) memberikan banyaknya node dari pohon PN}
# Basis 1: NbNELmt ((A)\) = 1
# Rekurens NbNELmt ((A,PN)) = 1 + NbELmt(PN)
def NbNElmt(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0
    # Jika hanya ada satu elemen(akar saja)
    elif isOneElmt(PN):
        return 1
    # Hitung 1 untuk akar, dan  rekursif pada setiap anak pohon.
    # Tanpa menggunakan loop, kita memanggil fungsi untuk setiap anak secara rekursif
    # Pertama pada anak pertama
    else:
        return 1 + NbNElmt(FirstElmt(anak(PN))) + NbNElmtChild(Tail(anak(PN)))
# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
def NbNElmtChild(PN):
    # Basis: Jika tidak ada anak
    if isTreeNEmpty(PN):
        return 0
    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    else:
        return NbNElmt(FirstElmt(PN)) + NbNElmtChild(Tail(PN))

# NbNDaun: PohonN-ner → integer ≥ 1
# {NbNDaun(PN) memberikan banyaknya jumlah daun dari pohon PN}
def NbNDaun(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0
     # Jika pohon adalah daun (anak kosong)
    elif isOneElmt(PN) and isTreeNEmpty(anak(PN)):
        return 1
    # Rekursi pada akar dan anak-anak
    else:
        return NbNDaunChild(anak(PN))
# Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak
def NbNDaunChild(PN):
     # Basis: Jika tidak ada anak
    if isTreeNEmpty(PN):
        return 0
    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    else:
        return NbNDaun(FirstElmt(PN)) + NbNDaunChild(Tail(PN))

# searchXTree: elemen, Tree -> boolean
# {searchXTree(x, PN) berfungsi untuk mencari elemen pada pohon PN, benar jika elemen terdapat dalam pohon PN}
def searchXTree(x, PN):
    if isTreeNEmpty(PN):
        return False
    elif FirstElmt(PN) == x:
        return True
    elif isTreeNEmpty(anak(PN)):
        return False
    else:
        return searchXTree(x, FirstElmt(anak(PN))) or searchXTreeChild(x, Tail(anak(PN)))
def searchXTreeChild(x, PN):
    if isTreeNEmpty(PN):
        return False
    else:
        return searchXTree(x, FirstElmt(PN)) or searchXTreeChild(x, Tail(PN))
  
# APLIKASI
T = makePN(2, [])
print(makePN(2, []))
print(isTreeNEmpty(T))
print(isOneElmt(T))
T2 = makePN(
    'A',
    [
        makePN('B',[makePN('D', []), makePN('E', []), makePN('F', [])]), makePN('C',[makePN('G',[]), makePN('H',[makePN('I',[])])])
    ]
)   
print(T2)
print(NbNElmt(T))
print(NbNElmt(T2))
print(NbNDaun(T))
print(NbNDaun(T2))
print(searchXTree('I', T2))
print(searchXTree('J', T2))
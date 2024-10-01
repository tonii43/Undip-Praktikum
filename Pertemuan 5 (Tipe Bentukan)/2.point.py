# Nama File : 2.point.py
# Deskripsi : membuat tipe bentukan point beserta konstruksi dan selektornya serta pengaplikasiannya
# Pembuat   : Muhammad Dimas Arya Putra - 24060124130062
# Tanggal   : 24 September 2023

from math import sqrt

# DEFINISI DAN SPESIFIKASI FUNGSI FX2
# fx2: integer --> integer
# {fx2(x) menghitung hasil pangkat 2 dari x}
# Realisasi dalam Python
def fx2(x):
    return x*x

# DEFINISI TYPE
# type point : <x:real, y:real>
# {<x, y> adalah sebuah point, dengan x adalah absis dan y adalah ordinat}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2 real --> point
# { MakePoint(x, y) membentuk sebuah point dari a dan b dengan a sebagai absis dan b sebagai ordinat} 
# Realisasi dalam Python
def makePoint(a, b):
    return [a, b]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Absis: point --> real
# {Absis(P) memberikan absis point P}
# Realisasi dalam Python
def absis(P):
    return P[0]

# Ordinat: point --> real
# {Ordinat(P) memberikan ordinat point P}
# Realisasi dalam Python
def ordinat(P):
    return P[1]

# InfoPoint: point --> string
# {InfoPoint(P) memberikan informasi absis dan ordinat P}
# Realisasi dalam Python
def infoPoint(P):
    return f"{absis(P), ordinat(P)}" 

# DEFINISI DAN SPESIFIKASI OPERATOR
# Jarak: 2 point --> real
# {Jarak(P1, P2) menghitung jarak antara 2 point P1 dan P2}
# Realisasi dalam Python
def jarak(P1, P2):
    return sqrt(fx2(absis(P1) - absis(P2)) + fx2(ordinat(P1) - ordinat(P2)))

# JarakO: point --> real
# {JarakO(P) menghitung jarak antara P dengan titik origin (0, 0)}
# Realisasi dalam Python
def jarakO(P):
    return sqrt(fx2(absis(P)) + fx2(ordinat(P)))

# Kuadran: point --> integer
# {Kuadran(P) mengembalikan kuadran di mana point P berada, dengan syarat P bukan titik (0, 0)
#  tidak terletak di sumbu X maupun sumbu Y}
# Realisasi dalam Python 
def kuadran(P):
    if absis(P) > 0 and ordinat(P) > 0:
        return 1
    elif absis(P) < 0 and ordinat(P) > 0:
        return 2
    elif absis(P) < 0 and ordinat(P) < 0:
        return 3
    elif absis(P) > 0 and ordinat(P) < 0:
        return 4

# Garis
def MakeGaris(P1, P2):
    return [P1, P2]

def point1(G):
    return G[0]
def point2(G):
    return G[1]

def gradien(G):
    return (ordinat(point1(G)) - ordinat(point2(G))) / (absis(point1(G)) - absis(point2(G)))
def panjangGaris(G):
    return sqrt((ordinat(point1(G)) - ordinat(point2(G)))**2 + (absis(point1(G)) - absis(point2(G)))**2)

def isSejajar(G1, G2):
    return gradien(G1) == gradien(G2)

#APLIKASI
print(kuadran(makePoint(1,2))) #--> 1
print(kuadran(makePoint(-1,2))) #--> 2
print(kuadran(makePoint(-1,-2))) #--> 3
print(kuadran(makePoint(1,-2))) #--> 4
print(jarak(makePoint(1,2), makePoint(2,3))) #--> 1.4142135623730951
print(jarakO(makePoint(1,2))) #--> 2.23606797749979
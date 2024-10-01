# Nama File : garis.py
# Deskipsi  : Membuat tipe bentukan garis beserta fungsi konstruktor, selektor, operator, dan predikatnya.
# Pembuat   : Mischa Nathanael Lumban Tobing
# NIM       : 24060124140175
# Tanggal   : 29 September 2024

# DEFINISI TYPE
# type point: <x: real, y: real>
#     {<x, y> merupakan tipe bentukan point.}
# type garis:  <p1: point, p2: point>
#     {<p1, p2> merupakan tipe bentukan garis.}
# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# --
# MakePoint: 2 real → point
#     {MakePoint(x, y) membentuk tipe data point dari input (x, y).}
# MakeGaris: 2 point → garis
#     {MakeGaris(p1, p2) membentuk tipe data garis dari input (p1, p2).}
# Realisasi:
def MakePoint(x, y):
    return [x, y]
def MakeGaris(p1, p2):
    return [p1, p2]
# -------------------------------------
# Definisi dan Spesifikasi Selektor
# --
# absis(p): point → real
#     {absis(p) mengembalikan absis dari point (p).}
# ordinat(p): point → real
#     {ordinat(p) mengembalikan ordinat dari point (p).}
# getPoint1(g): garis → point 
#     {getPoint1(g) mengembalikan titik awal dari garis (g).}
# getPoint2(g): garis → point 
#     {getPoint2(g) mengembalikan titik akhir dari garis (g).}
# Realisasi:
def absis(p):
    return p[0]
def ordinat(p):
    return p[1]

def getPoint1(g):
    return g[0]
def getPoint2(g):
    return g[1]
# -------------------------------------
# Definisi dan Spesifikasi Predikat
# --
# isSejajar: 2 garis → boolean
#     {isSejajar(g1, g2) akan bernilai true apabila (g1) sejajar dengan (g2).}
# Realisasi:
def isSejajar(g1, g2):
    return gradien(g1) == gradien(g2)
# -------------------------------------
# Definisi dan Spesifikasi Operator
# --
# gradien: garis → real
#     {gradien(g) akan mengembalikan gradien dari garis (g).}
# panjangGaris: garis → real
#     {panjangGaris(g) akan mengembalikan panjang dari garis (g).}
# Realisasi:
def gradien(g):
    return (ordinat(getPoint1(g)) - ordinat(getPoint2(g))) / (absis(getPoint1(g)) - absis(getPoint2(g)))
def panjangGaris(g):
    return ((ordinat(getPoint1(g)) - ordinat(getPoint2(g)))**2 + (absis(getPoint1(g)) - absis(getPoint2(g)))**2) ** .5
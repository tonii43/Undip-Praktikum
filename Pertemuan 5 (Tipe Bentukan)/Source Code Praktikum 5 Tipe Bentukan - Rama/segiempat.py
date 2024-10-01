# Nama File : segiempat.py
# Deskipsi  : Membuat tipe bentukan segiempat beserta fungsi konstruktor, selektor, operator, dan predikatnya.
# Pembuat   : Mischa Nathanael Lumban Tobing
# NIM       : 24060124140175
# Tanggal   : 29 September 2024

# DEFINISI TYPE
# type point: <x: real, y: real>
#     {<x, y> merupakan tipe bentukan point.}
# type SegiEmpat:  <p1: point, p2: point, p3: point, p4: point>
#     {<p1, p2, p3, p4> merupakan tipe bentukan SegiEmpat, dengan asumsi bahwa p1 adalah titik kiri bawah,
#      p2 adalah titik kanan bawah, p3 adalah titik kanan atas, dan p4 adalah titik kiri atas.}
# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# --
# MakePoint: 2 real → point
#     {MakePoint(x, y) membentuk tipe data point dari input (x, y).}
# MakeSegiEmpat: 4 point → SegiEmpat
#     {MakeSegiEmpat(p1, p2, p3, p4) membentuk tipe data segiempat dari input (p1, p2, p3, p4).}
# Realisasi:
def MakePoint(x, y):
    return [x, y]
def MakeSegiEmpat(p1, p2, p3, p4):
    return [p1, p2, p3, p4]
# -------------------------------------
# Definisi dan Spesifikasi Selektor
# --
# absis(p): point → real
#     {absis(p) mengembalikan absis dari point (p).}
# ordinat(p): point → real
#     {ordinat(p) mengembalikan ordinat dari point (p).}
# getPoint1(g): SegiEmpat → point 
#     {getPoint1(g) mengembalikan titik 1 dari SegiEmpat (g).}
# getPoint2(g): SegiEmpat → point 
#     {getPoint2(g) mengembalikan titik 2 dari SegiEmpat (g).}
# getPoint3(g): SegiEmpat → point 
#     {getPoint3(g) mengembalikan titik 3 dari SegiEmpat (g).}
# getPoint4(g): SegiEmpat → point 
#     {getPoint4(g) mengembalikan titik 4 dari SegiEmpat (g).}
# Realisasi:
def absis(p):
    return p[0]
def ordinat(p):
    return p[1]

def getPoint1(g):
    return g[0]
def getPoint2(g):
    return g[1]
def getPoint3(g):
    return g[2]
def getPoint4(g):
    return g[3]
# -------------------------------------
# Definisi dan Spesifikasi Predikat
# --
# isBujurSangkar: SegiEmpat → boolean
#     {isBujurSangkar(se) akan bernilai true apabila (se) adalah segiempat berbentuk bujur sangkar.}
# isJajarGenjang: SegiEmpat → boolean
#     {isJajarGenjang(se) akan bernilai true apabila (se) adalah segiempat berbentuk jajar genjang.}
# Realisasi:
def isBujurSangkar(se):
    if (panjangGaris(getPoint1(se), getPoint2(se)) == 
        panjangGaris(getPoint3(se), getPoint4(se)) == 
        panjangGaris(getPoint1(se), getPoint4(se)) == 
        panjangGaris(getPoint2(se), getPoint3(se))):
        return (panjangGaris(getPoint1(se), getPoint3(se)) == 
                panjangGaris(getPoint2(se), getPoint4(se)))
    else:
        return False
    
def isJajarGenjang(se):
    return (panjangGaris(getPoint1(se), getPoint2(se)) == 
            panjangGaris(getPoint3(se), getPoint4(se)) and 
            panjangGaris(getPoint1(se), getPoint4(se)) == 
            panjangGaris(getPoint2(se), getPoint3(se)) and 
            gradien(getPoint1(se), getPoint2(se)) == 
            gradien(getPoint3(se), getPoint4(se)) and 
            gradien(getPoint1(se), getPoint4(se)) == 
            gradien(getPoint2(se), getPoint3(se)) and
            gradien(getPoint1(se), getPoint2(se)) * gradien(getPoint2(se), getPoint3(se)) != -1 and
            gradien(getPoint3(se), getPoint4(se)) * gradien(getPoint4(se), getPoint1(se)) != -1)
# -------------------------------------
# Definisi dan Spesifikasi Operator
# --
# gradien: 2 point → real
#     {gradien(g) akan mengembalikan gradien dari garis dengan titik (p1, p2).}
# panjangGaris: 2 point → real
#     {panjangGaris(p1, p2) akan mengembalikan panjang dari garis dengan titik (p1, p2).}
# Realisasi:
def gradien(p1, p2):
    if ((absis(p1) - absis(p2)) == 0):
        return 0
    else:
        return (ordinat(p1) - ordinat(p2)) / (absis(p1) - absis(p2))
def panjangGaris(p1, p2):
    return ((ordinat(p1) - ordinat(p2))**2 + (absis(p1) - absis(p2))**2) ** .5
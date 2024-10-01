# Nama File : pecahan.py
# Deskipsi  : Membuat tipe bentukan pecahan beserta fungsi konstruktor, selektor, operator, dan predikatnya.
# Pembuat   : Mischa Nathanael Lumban Tobing
# NIM       : 24060124140175
# Tanggal   : 29 September 2024

# DEFINISI TYPE
# type pecahan:  <pembilang: integer, penyebut: integer > 0>
#     {<pembilang, penyebut> merupakan tipe bentukan pecahan.}
# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# --
# MakePecahan: integer, integer > 0 → pecahan
#     {MakePecahan(pembilang, penyebut) membentuk tipe data pecahan dari input (pembilang, penyebut).}
# Realisasi:
def MakePecahan(pembilang, penyebut):
    return [pembilang, penyebut]
# -------------------------------------
# Definisi dan Spesifikasi Selektor
# --
# pembilang: pecahan → integer
#     {pembilang(p) mengembalikan pembilang dari pecahan (p).}
# penyebut: pecahan → integer > 0
#     {penyebut(p) mengembalikan penyebut dari pecahan (p).}
# Realisasi:
def pembilang(p):
    return p[0]

def penyebut(p):
    return p[1]
# -------------------------------------
# Definisi dan Spesifikasi Predikat
# --
# IsEq: 2 pecahan → boolean
#     {IsEq(p1, p2) akan bernilai true apabila (p1) ekuivalen dengan (p2).}
# IsLs: 2 pecahan → boolean
#     {IsLs(p1, p2) akan bernilai true apabila (p1) lebih kecil dari (p2).}
# IsGrt: 2 pecahan → boolean
#     {IsGrt(p1, p2) akan bernilai true apabila (p1) lebih besar dari (p2).}
# Realisasi:
def IsEq(p1, p2):
    return pembilang(p1) * penyebut(p2) == penyebut(p1) * pembilang(p2)
def IsLs(p1, p2):
    return pembilang(p1) * penyebut(p2) < penyebut(p1) * pembilang(p2)
def IsGrt(p1, p2):
    return pembilang(p1) * penyebut(p2) > penyebut(p1) * pembilang(p2)
# -------------------------------------
# Definisi dan Spesifikasi Operator
# --
# AddP: 2 pecahan → pecahan
#     {AddP(p1, p2) akan mengembalikan hasil penjumlahan dari (p1, p2).}
# SubP: 2 pecahan → pecahan
#     {SubP(p1, p2) akan mengembalikan hasil pengurangan dari (p1, p2).}
# MulP: 2 pecahan → pecahan
#     {MulP(p1, p2) akan mengembalikan hasil perkalian dari (p1, p2).}
# DivP: 2 pecahan → pecahan
#     {DivP(p1, p2) akan mengembalikan hasil pembagian dari (p1, p2).}
# Real: pecahan → real
#     {Real(p) akan mengembalikan hasil pembagian pembilang dengan penyebut pada pecahan (p).}
# Realisasi:
def AddP(p1, p2):
    return MakePecahan(penyebut(p2) * pembilang(p1) + penyebut(p1) * pembilang(p2), penyebut(p1) * penyebut(p2))
def SubP(p1, p2):
    return MakePecahan(penyebut(p2) * pembilang(p1) - penyebut(p1) * pembilang(p2), penyebut(p1) * penyebut(p2))
def MulP(p1, p2):
    return MakePecahan(pembilang(p1) * pembilang(p2), penyebut(p1) * penyebut(p2))
def DivP(p1, p2):
    return MakePecahan(pembilang(p1) * penyebut(p2), pembilang(p2) * penyebut(p1))
def Real(p):
    return pembilang(p) / penyebut(p)

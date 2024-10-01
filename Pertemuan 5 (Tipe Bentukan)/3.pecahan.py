#Nama File : 3.pecahan.py
#Deskripsi : membuat tipe bentukan pecahan beserta konstruksi dan selektornya serta pengaplikasiannya
#Pembuat   : Muhammad Dimas Arya Putra - 24060124130062
#Tanggal   : 24 September 2023

#DEFINISI TYPE
#type pecahan : <x:integer, y:integer>
#<x,y> adalah sebuah pecahan, dengan x adalah pembilang dan y adalah penyebut

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR

#make_pecahan: 2 integer --> array
#make_pecahan(a,b) membentuk sebuah array dari a dan b dengan a sebagai 
#pembilang dan b sebagai penyebut
#Realisasi fungsi make_pecahan
def make_pecahan (a,b) :
    return [a,b]
   
#pemb: 2 integer --> array
#pemb (P) mengembalikan komponen array ke-0 dari P
#Realisasi fungsi pemb
def pemb (P) :
    return P[0]
   
#pemb: 2 integer --> array
#pemb (P) mengembalikan komponen array ke-1 dari P
#Realisasi fungsi peny
def peny (P) :
    return P[1]

#AddP: 2 pecahan --> pecahan
#AddP (P1,P2) menjumlahkan dua buah pecahan P1 dan P2
#Realisasi fungsi AddP
def AddP (P1,P2) :
    return make_pecahan(pemb(P1) * peny(P2) + pemb(P2) * peny(P1), peny(P1) * peny(P2))
   
#SubP: 2 pecahan --> pecahan
#SubP (P1,P2) mmengurangkan dua buah pecahan P1 dan P2
#Realisasi fungsi SubP
def SubP (P1, P2) :
    return make_pecahan(pemb(P1) * peny(P2) - pemb(P2) * peny(P1), peny(P1) * peny(P2))
   
#MulP : 2 pecahan --> pecahan
#MulP (P1,P2) mengalikan dua buah pecahan P1 dan P2
#Realisasi fungsi MulP
def MulP (P1,P2) :
    return make_pecahan(pemb(P1) * pemb(P2), peny(P1) * peny(P2))
   
#DivP : 2 pecahan --> pecahan
#DivP (P1,P2) membagi dua buah pecahan P1 dan P2
#Realisasi fungsi DivP
def DivP (P1,P2) :
    return make_pecahan(pemb(P1) * peny(P2), peny(P1) * pemb(P2))
   
#REalP : 1 pecahan --> real
#REalP (P) menuliskan pecahan dalam bentuk notasi desimal
#Realisasi fungsi RealP
def RealP (P) :
    return pemb(P)/peny(P)
   
#IsEqP : 2 pecahan --> boolean
#IsEqP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 sama dengan P2
#Realisasi fungsi IsEqP
def IsEqP (P1,P2) :
    return pemb(P1) * peny(P2) == peny(P1) * pemb(P2)
   
#IsLtP : 2 pecahan --> boolean
#IsLtP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 lebih kecil P2
#Realisasi fungsi IsLtP
def IsLtP (P1,P2) :
    return pemb(P1) * peny(P2) < peny(P1) * pemb(P2)
   
#IsGtP : 1 pecahann --> boolean
#IsGtP (P1,P2) membandingkan dua buah pecahan apakah nilai P1 lebih besar P2
#Realisasi fungsi IsGtP
def IsGtP (P1,P2) :
    return pemb(P1) * peny(P2) > peny(P1) * pemb(P2)

#APLIKASI
P = make_pecahan (1,2)
Q = make_pecahan (1,2)
print (pemb(P)) #--> 1
print (peny(P)) #--> 2
print (AddP(P,Q)) #--> [4, 4]
print (SubP(P,Q)) #--> [0, 4]
print (MulP(P,Q)) #--> [1, 4]
print (DivP(P,Q)) #--> [2, 2]
print (RealP(P)) #--> 0.5
print (IsEqP(P,Q)) #--> True
print (IsLtP(P,Q)) #--> False
print (IsGtP(P,Q)) #--> False
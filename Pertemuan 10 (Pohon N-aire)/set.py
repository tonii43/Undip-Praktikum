# Nama File : set.py
# Deskripsi : berisi type dan operasi set yang menggunakan list
# Pembuat   : Muhammad Dimas Arya Putra - 24060124130062
# Tanggal   : 5 November 2024

from list import *

# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN

# Rember: elemen, list -> list
# Rember(x,L) menghapus sebuah elemen x dari list L
#   Jika x ada di list L, maka elemen L berkurang 1.
#   Jika x tidak ada di list L maka L tetap.
#   List kosong tetap menjadi list kosong.
def Rember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember(x, Tail(L)))
        
# APLIKASI
# print(Rember(2, []))
# print(Rember(2, [3]))
# print(Rember(2, [3,4,5,6,2,3,5,7,8,2]))

# MultiRember: elemen, list -> list
# MultiRember(x,L) menghapus semua kemunculan elemen x dari list L.
#   List baru yang dihasilkan tidak lagi memiliki elemen x.
#   List kosong tetap menjadi list kosong.
def MultiRember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))
        
# APLIKASI
# print(MultiRember(2, []))
# print(MultiRember(2, [3]))
# print(MultiRember(2, [3,4,5,6,2,3,5,7,8,2]))

# DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST

# MakeSet: list -> set
# MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali
#   list kosong tetap menjadi himpunan kosong
def MakeSet(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSet(Tail(L)))

def MakeSetv2(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), MakeSetv2(MultiRember(FirstElmt(L), Tail(L))))

# APLIKASI
# print(MakeSet([3,4,5,2,3,5,7,8,2]))
# print(MakeSetv2([3,4,5,2,3,5,7,8,2]))

# DEFINISI DAN SPESIKASI KONSTRUKTOR SET

# KonsoSet: elemen,set -> set
#   KonsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H
#   dengan syarat e belum ada di dalam himpunan H
def KonsoSet(e, H):
    if IsMember(e, H):
        return H
    else:
        return Konso(e, H)
    
# APLIKASI
# print(KonsoSet(1, [2,3,4]))
# print(KonsoSet(2, [2,3,4]))

# DEFINISI DAN SPESIFIKASI PREDIKAT

# IsSet: list -> boolean
#   IsSet(L) mengembalikan true jika L adalah sebuah set
def IsSet(L):
    if IsEmpty(L):
        return True
    else:  
        if IsMember(FirstElmt(L), Tail(L)):
            return False
        else:
            return IsSet(Tail(L))
        
# APLIKASI
# print(IsSet([1,2,3]))
# print(IsSet([1,2,2]))

# IsSubset: 2 set -> boolean
#   IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2
def IsSubset(H1, H2):
    if IsEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1), H2):
            return IsSubset(Tail(H1), H2)
        else:
            return False

# APLIKASI
# print(IsSubset([1,2,3], [1,2,3,4]))
# print(IsSubset([1,2,3], [1,2]))

# IsEqualSet: 2 set -> boolean
#   IsEqualSet(H1,H2} benar jika H1 adalah set yang sama dengan H2
def IsEqualSet(H1, H2):
    if IsEmpty(H1):
        return True
    else:
        if IsMember(FirstElmt(H1), H2):
            return IsEqualSet(Tail(H1), H2)
        else:
            return False
        
# APLIKASI
# print(IsEqualSet([1,2,3], [1,2,3]))
# print(IsEqualSet([1,2,3], [1,2,4]))

# IsIntersect: 2 set -> boolean
#   IsIntersect(H1,H2) benar jika H1 beririsan dengan H2
def IsIntersect(H1, H2):
    if IsEmpty(H1):
        return False
    else:
        if IsMember(FirstElmt(H1), H2):
            return True
        else:
            return IsIntersect(Tail(H1), H2)
        
# APLIKASI
# print(IsIntersect([1,2,3],[3,4,5]))
# print(IsIntersect([1,2,3],[4,5,6]))

#DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN

# MakeIntersect: 2 set -> set
#   MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2
def MakeIntersect(H1, H2):
    if IsEmpty(H1):
        return []
    else:
        if IsMember(FirstElmt(H1), H2):
            return Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
        else:
            return MakeIntersect(Tail(H1),H2)
        
# APLIKASi
# print(MakeIntersect([1,2,3],[3,4,5]))
# print(MakeIntersect([1,2,3],[4,5,6]))

# MakeUnion: 2 set -> set
#   MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2
def MakeUnion(H1, H2):
    if IsEmpty(H1):
        return H2
    else:
        if IsMember(FirstElmt(H1), H2):
            return MakeUnion(Tail(H1), H2)
        else:
            return Konso(FirstElmt(H1), MakeUnion(Tail(H1), H2))
        
# APLIKASI
# print(MakeUnion([1,2,3],[3,4,5]))
# print(MakeUnion([1,2,3],[4,5,6]))

# NBIntersect: 2 set -> integer
#   NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
#   tanpa memanfaatkan fungsi MakeIntersect(H1,H2).
def NBIntersect(H1, H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return 0
    else:
        if IsMember(FirstElmt(H1), H2):
            return 1 + NBIntersect(Tail(H1), H2)
        else:
            return 0 + NBIntersect(Tail(H1), H2)

# APLIKASI        
# print(NBIntersect([1,2,3],[3,4,5]))
# print(NBIntersect([1,2,3],[4,5,6]))
# print(NBIntersect([1,2,3],[6,5,3]))

# NBUnion: 2 set -> integer
#   NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2
#   tanpa memanfaatkan fungsi MakeUnion(H1,H2).
def NBUnion(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return 0
    elif IsEmpty(H1) and not IsEmpty(H2):
        return NbElmt(H2)
    elif not IsEmpty(H1) and IsEmpty(H2):
        return NbElmt(H1)
    elif IsMember(FirstElmt(H1), H2):
        return NBUnion(Tail(H1), H2)
    else:
        return 1 + NBUnion(Tail(H1), H2)

# APLIKASI
# print(NBUnion([1,2,3],[]))
# print(NBUnion([1,2,3],[4,5,6]))
# print(NBUnion([1,2,3],[6,2,3]))
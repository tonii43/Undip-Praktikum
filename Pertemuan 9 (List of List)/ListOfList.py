# Nama              : Muhammad Dimas Arya Putra
# NIM               : 24060124130062
# Deskripsi Fungsi  : List of List

from list import *
from set import *

#Konstruktor

# DEFINISI DAN SPESIFIKASI
# KonsLo(e, L): elemen, List of List --> List of List
# KonsLo(e, L) Menambahkan elemen di baris awal List of List
def KonsLo(e, L):
    return [e] + L

# DEFINISI DAN SPESIFIKASI
# KonsLi(L, e): List of List, elemen --> List of List
# KonsLi(L, e) Menambah6y5ukan elemen di baris akhir List of List
def KonsLi(L, e):
    return L + [e]

# Selektor

# DEFINISI DAN SPESIFIKASI
# FirstList(L): List of List --> elemen
# FirstList(L) Menampilkan elemen pertama dari List of List
def FirstList(L):
    return L[0]

# DEFINISI DAN SPESIFIKASI
# LastList(L): List of List --> elemen
# LastList(L) Menampilkan elemen terakhir dari List of List
def LastList(L):
    return L[-1]

# DEFINISI DAN SPESIFIKASI
# HeadList(L): List of List --> List of List
# HeadList(L) List of List dengan menghilangkan elemen terakhirnya
def HeadList(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI
# TailList(L): List of List --> List of List
# TailList(L) List of List dengan menghilangkan elemen pertamanya
def TailList(L):
    return L[1:]

# Predikat

# DEFINISI DAN SPESIFIKASI
# isEmpty(L): List of List --> boolean
# isEmpty(L) mengecek apakah List of List kosong
def IsEmpty(L):
    return L == []

# DEFINISI DAN SPESIFIKASI
# IsAtom: List of List --> boolean
# IsAtom Cek apakah S adalah atom atau bukan sebuah list
def IsAtom(S):
    return type(S) != list

# DEFINISI DAN SPESIFIKASI
# IsList: List of List --> boolean
# IsList Cek apakah S adalah List
def IsList(S):
    return type(S) == list

# PREDIKAT

# DEFINISI DAN SPESIFIKASI
# IsList: 2 List of List --> boolean
# IsList Cek apakah S adalah List
# Realisasi dalam Python
def IsMemberLS(L, S):
    if IsEmpty(S):
        return False
    else:
        if(IsAtom(FirstList(S))):
            return IsMemberLS(L, TailList(S))
        else:
            if IsEqual(FirstList(S), L):
                return True
            else:
                return IsMemberLS(L, TailList(S))

# APLIKASI
print(IsMemberLS([3,1],[1,2,[3,1]]))
print(IsMemberLS([1],[1,2,3,[4,5]]))

# DEFINISI DAN SPESIFIKASI
# IsList: 2 List of List --> boolean
# IsList Cek apakah S adalah List
# Realisasi dalam Python
def IsEqS(S1, S2):
    if IsEmpty(S1) and IsEmpty(S2):
        return True
    elif not IsEmpty(S1) and IsEmpty(S2):
        return False
    elif IsEmpty(S1) and not IsEmpty(S2):
        return False
    else:
        if (IsAtom(FirstList(S1)) and IsAtom(FirstList(S2))):
            if (FirstList(S1) == FirstList(S2)):
                return IsEqS(TailList(S1), TailList(S2))
            else:
                return False
        elif (IsList(FirstList(S1)) and IsList(FirstList(S2))):
            return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(TailList(S1), TailList(S2))
        else:
            return False

# APLIKASI
print(IsEqS([[1,2],3,4,5],[[1,2],3,4,5]))
print(IsEqS([[1,2],3,4,5],[[1],3,4,5]))

# DEFINISI DAN SPESIFIKASI
# IsMemberS: elemen, list of list-> boolean
# IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S
# Realisasi dalam Python
def IsMemberS(x, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            if x == FirstList(S):
                return True
            else:
                return IsMemberS(x, TailList(S))
        elif IsList(FirstList(S)):
            return IsMemberS(x, FirstList(S)) or IsMemberS(x, TailList(S))

# APLIKASI
print(IsMemberS(3, []))
print(IsMemberS(3, [2,4,3, [1], [4,5]]))
print(IsMemberS(3, [2,4,7, [1], [3,5]]))

# OPERASI/FUNGSI LOL

# DEFINISI DAN SPESIFIKASI
# Rember: elemen, list of list -> list of list
# Rember(x,S) menghapus semua elemen x yang ada di list of list S
# Realisasi dalam Python
def Rember(x, S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) == x:
                return Rember(x, TailList(S))
            else:
                return KonsLo(FirstList(S), Rember(x, TailList(S)))
        elif IsList(FirstList(S)):
            if FirstList(S) == x:
                return Rember(x, TailList(S))
            else:
                return KonsLo(Rember(x, FirstList(S)), Rember(x, TailList(S)))

# APLIKASI
print(Rember(3, []))
print(Rember(3, [4, 3, [2,4], 3]))
print(Rember(3, [2, 4, [3,6,9], 5, 3]))

# DEFINISI DAN SPESIFIKASI
# Max: list of list -> elemen
# Max(S) mengembalikan elemen maksimum di dalam list of list S
# Realisasi dalam Python
def Max(S):
    if IsEmpty(S):
        return []
    elif IsAtom(S):
        return S
    elif IsOneElmt(S):
        return Max(FirstList(S))
    else:
        return max2(Max(FirstList(S)), Max(TailList(S)))

# APLIKASI
print(Max([4, 5, 6, [8,9,10], [12,0], 8]))
print(Max([4, 15, 6, [8,9,10], [12,0], 8]))

# DEFINISI DAN SPESIFIKASI
# NBElmtAtom: list of list -> integer
# NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom
# Realisasi dalam Python
def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return 1 + NBElmtAtom(TailList(S))
    elif IsList(FirstList(S)):
        return 0 + NBElmtAtom(TailList(S))
    
# APLIKASI
print(NBElmtAtom([4, 5, 6, [8,9,10], [12,0], 8]))
print(NBElmtAtom([4, 15, 6, [8,9], 10, [12], 8]))
print(NBElmtAtom([[8,9,10]]))

# DEFINISI DAN SPESIFIKASI
# NBElmtList: list of list -> integer
# NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list
# Realisasi dalam Python
def NBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return 0 + NBElmtList(TailList(S))
    elif IsList(FirstList(S)):
        return 1 + NBElmtList(TailList(S))
    
# APLIKASI
print(NBElmtList([4, 5, 6, [8,9,10], [12,0], 8]))
print(NBElmtList([[4, 15], 6, [8,9], 10, [12], 8]))
print(NBElmtList([[8,9,10]]))

# DEFINISI DAN SPESIFIKASI
# SumLoL: list of list -> integer
# SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S
# Realisasi dalam Python
def SumLoL(S):
    if IsEmpty(S):
        return 0
    elif IsEmpty(FirstList(S)):
        return 0
    elif IsAtom(FirstList(S)):
        return FirstList(S) + SumLoL(TailList(S))
    elif IsList(FirstList(S)):
        return SumLoL(FirstList(S)) + SumLoL(TailList(S))
    
# APLIKASI
print(SumLoL([[]]))
print(SumLoL([4, 5, 6, [2,3,1]]))
print(SumLoL([[2,3,4]]))

# DEFINISI DAN SPESIFIKASI
# MaxNBElmtList: list of list -> integer
# MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S
# Realisasi dalam Python
def MaxNBElmtList(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return MaxNBElmtList(TailList(S))
    elif IsList(FirstList(S)):
        return max2(NbElmt(FirstList(S)), MaxNBElmtList(TailList(S)))

print(MaxNBElmtList([[4,5,6,7], [8,9,10], [12,0], 8]))
print(MaxNBElmtList([[4,15], 6, [8,9], 10, [12], 8]))
print(MaxNBElmtList([8,9,10]))

# DEFINISI DAN SPESIFIKASI
# MaxSumElmt: list of list -> integer
# MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S
# jika elemen berupa list, maka dihitung jumlahan elemen dalam list tersebut5
# jika elemen atom, maka nilainya adalah elemen tersebut
# Realisasi dalam Python
def MaxSumElmt(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstList(S)):
        return max2(FirstList(S), MaxSumElmt(TailList(S)))
    elif IsList(FirstList(S)):
        return max2(SumLoL(FirstList(S)), MaxSumElmt(TailList(S)))

# APLIKASI
print(MaxSumElmt([[1,2], 9, [4,5,6], 8]))
print(MaxSumElmt([[1,2], 90, [4,5,6], 8]))
print(MaxSumElmt([8,9,10]))
print(MaxSumElmt([[8,9,10]]))
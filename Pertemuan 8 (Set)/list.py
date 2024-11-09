# Nama File : 1.list.py
# Deskripsi : berisi type dan operasi list
# Pembuat   : Muhammad Dimas Arya Putra
# NIM       : 24060124130062
# Tanggal   : 29 Oktober 2024

# DEFINISI DAN SPESIFIKASI TYPE
# Konstruktor menambahkan elemen di awal, notasi prefix
# type List: [] atau  [e o List]
# Konstruktor menambahkan elemen di akhir, notasi postfix
# type List: [] atau [List o e]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List --> List
#   {Konso(e,L) menghasilkan sebuah List dari e dan L dengan e sebagai elemen pertama}
# REALISASI 
def Konso(e,L):
    return [e]+L

# Konsi: List, elemen --> List
#   {Konsi(L,e) menghasilkan sebuah List dari L dan e dengan e sebagai elemen terakhir}
# Realisasi
def Konsi(L,e):
    return L + [e]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong --> elemen
#   {FirstElmt(L) mengembalikan elemen pertama dari list L}
# Realisasi
def FirstElmt(L):
    return L[0]

# LastElmt: List tidak kosong --> elemen
#   {LastElmt(L): mengembalikan elemen terakhir terakhir list L}
# Realisasi
def LastElmt(L):
    return L[-1]

# Head: List tidak kosong --> List
#   {Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong}
# Realisasi
def Head(L):
    return L[:-1]

# Tail: List tidak kosong --> List
#   {Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong}
# Realisasi
def Tail(L):
    return L[1:]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List --> boolean
#   {IsEmpty(L) benar jika list kosong}
# Realisasi
def IsEmpty(L):
    return L == []

# IsOneElmt: List --> boolean
#   {IsOneElmt(L) adalah benar jika list L hanya mempunyai satu elemen}
# Realisasi
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L)==[] and Head(L)==[]

# IsMember: elemen, List --> boolean 
#   {IsMember(X,L) adalah benar jika X adalah anggota elemen List L}
# Realisasi
def IsMember(X,L):
    if IsEmpty(L):
        return False
    elif X==FirstElmt(L):
        return True
    else:
        return IsMember(X,Tail(L))

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt: List --> integer
#   {NbElmt(L) Menghasilkan banyaknya elemen list, nol jika kosong}
# Realisasi
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
# ElmtKeN: integer >= 0, List --> elemen
#   {ElmtKeN(N,L) mengembalikan elemen ke N dari list L, N <= NbElmt(L) dan N>=0}
# Realisasi
def ElmtKeN(N,L):
    if N==1:
        return FirstElmt(L)
    else:
        return ElmtKeN(N-1,Tail(L))

# Copy: List --> List 
#   {Copy(L) menghasilkan list yang identik dengan list L}
# Realisasi
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L),Copy(Tail(L)))

# Invers: List --> List
#   {Invers(L) menghasilkan List L yang dibalik}
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(LastElmt(L),Inverse(Head(L)))

# Konkat : 2 List --> List
#   {Konkat(L1,L2) menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1}
# Realisasi
def Konkat(L1,L2):
    return Copy(L1)+Copy(L2)
    
# SumElmt: List of integer --> integer
#   {SumElmt(L) menghasilkan jumlahan dari setiap elemen di dalam list L}
# Realisasi
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# AvgElmt: List of integer --> integer
#   {AvgElmt(L) menghasilkan nilai rata-rata}
# Realisasi 
def AvgElmt(L):
    return SumElmt(L)//NbElmt(L)

# MaxElmt: List of integer --> integer
#   {MaxElmt(L) mengembalikan elemen maksimum dari list L}
def max2(a,b):
    return ((a + b) + abs(a - b)) // 2
# Realisasi
def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        return max2(FirstElmt(L),MaxElmt(Tail(L)))
    
# MaxNB:List of integer -> <integer, integer>
# MaxNB(L) menghasilkan <max, countMax>
#   dengan max adalah elemen maksimum list L
#   dan countMax adalah banyaknya kemunculan max di list L
# Realisasi
def countMax(L):
    def countMaxHelper(L, max):
        if IsEmpty(L):
            return 0
        elif FirstElmt(L) == max:
            return 1 + countMaxHelper(Tail(L), max)
        else:
            return countMaxHelper(Tail(L), max)
    return countMaxHelper(L, MaxElmt(L))

def MaxNB(L):
    return [MaxElmt(L), countMax(L)]

# AddList: 2 List of integer -> List of integer
# AddList(L1,L2) menghasilkan list baru yang setiap elemennya
#   adalah hasil penjumlahan setiap elemen di L1 dan L2 pada posisi yang sama
# Realisasi
def AddList(L1,L2):
    if IsEmpty(L1):
        return L2
    else:
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

# IsPalindrom(L): List of character -> boolean
# IsPalindrom(L) benar jika L merupakan kata palindrom
#   yaitu kata yang sama jika dibaca dari kiri atau kanan
# Realisasi
def IsPalindrom(L):
    if IsEmpty(L):
        return True
    elif FirstElmt(L) != LastElmt(L):
        return False
    else:
        return IsPalindrom(Tail(Head(L)))
        
# APLIKASI
# print(Konso(2,[3]))
# print(Konsi([3,4,5],6))
# print(FirstElmt([3,4,5,6,7]))
# print(LastElmt([3,4,5,6,7]))
# print(Tail([3,4,5,6,7]))
# print(Head([3,4,5,6,7]))
# print(ElmtKeN(3, [9,10,2,4,5]))
# print(IsEmpty([]))
# print(IsEmpty( [3,4, 5,6,7]))
# print(IsMember(3, [2,3,4]))
# print(IsOneElmt([]))
# print(IsOneElmt([3]))
# print(IsOneElmt([3,4,5,6,7]))
# print(NbElmt([3,4,5,6,7]))
# print(Konkat([1,2,3],[4,5,6]))
# print(SumElmt([1,2,3]))
# print(AvgElmt([1,2,3]))
# print(Copy([1,2,3]))
# print(Inverse([1,2,3]))
# print(Konkat([1,2,3],[3,4,5]))
# print(MaxNB([3,2,3,4,5,5,5]))
# print(AddList([1,2,3],[3,4,5]))
# print(IsPalindrom(['malam']))
# print(MaxNB([9,1,4,4,4]))
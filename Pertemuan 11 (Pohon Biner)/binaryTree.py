from ListOfList1 import *

# DEFINISI TYPE
# Type PohonBiner: <A: integer, L: PohonBiner, R: PohonBiner>
# Pohon Biner terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePB: integer, 2 PohonBiner --> PohonBiner
# MakePB(A, L, R) membuat Pohon Biner yang terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan
# REALISASI
def MakePB(A, L, R):
    return [A, L, R]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar: PohonBiner --> integer
# Akar(P) mengembalikan akar dari sebuah PohonBiner
# REALISASI
def Akar(P):
    return P[0] 

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Left: PohonBiner --> PohonBiner
# Left(P) mengembalikan subpohon kiri dari sebuah PohonBiner
# REALISASI
def Left(P):
    return P[1] 

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Right: PohonBiner --> PohonBiner
# Right(P) mengembalikan subpohon kanan dari sebuah PohonBiner
# REALISASI
def Right(P):
    return P[2] 

def IsTreeEmpty(T):
    return T == []

def IsOneElmt(T):
    return not IsTreeEmpty(T) and IsTreeEmpty(Left(T)) and IsTreeEmpty(Right(T))

# IsUnerLeft : PohonBiner → boolean
# {IsUnerLeft(P) true jika P hanya mengandung sub pohon kiri tidak kosong: (//L A \\) } 
def IsUnerLeft(T) :
    return (not IsTreeEmpty(Left(T))) and (IsTreeEmpty(Right(T)))

# IsUnerRight : PohonBiner → boolean
# {IsUnerRight (P) true jika P hanya mengandung sub pohon kanan tidak kosong: (//A R\\) }
def IsUnerRight(T) :
    return (IsTreeEmpty(Left(T))) and (not IsTreeEmpty(Right(T)))

# IsBiner : PohonBiner tidak kosong → boolean
# {IsBiner(P) true jika P mengandung sub pohon kiri dan sub pohon kanan : 
# (//L A R\\) } 
def IsBiner(T) :
    return (not IsTreeEmpty(Left(T))) and (not IsTreeEmpty(Right(T)))

# IsExistLeft : PohonBiner tidak kosong → boolean
# {IsExistLeft (P) true jika P mengandung sub pohon kiri }
def IsExistLeft(T) :
    return (not IsTreeEmpty(Left(T)))

# IsExistRight : PohonBiner tidak kosong → boolean
#  {ExistRight(P) true jika P mengandung sub pohon kanan }
def IsExistRight(T) :
    return (not IsTreeEmpty(Right(T)))
    

def PrintBinaryTreeHelp(T, indent):
    if T != []:
        print(indent + str(Akar(T)))
        PrintBinaryTreeHelp(Left(T), indent + '\t')
        PrintBinaryTreeHelp(Right(T), indent + '\t')
    else:
        print(indent + "[]")

def PrintBinaryTree(T):
    PrintBinaryTreeHelp(T, '')

def NbElmtTree(T):
    if IsTreeEmpty(T):
        return 0
    else:
        return NbElmtTree(Left(T)) + 1 + NbElmtTree(Right(T))

def NbDaun(T) :
    if IsTreeEmpty(T):
        return 0
    elif IsOneElmt(T) :
        print(Akar(T))
        return 1
    # elif (not IsEmpty(Left(T))) and (IsEmpty(Right(T))) :
    #     return NbDaun(Left(T))
    # elif (IsEmpty(Left(T))) and (not IsEmpty(Right(T))) :
    #     return NbDaun(Right(T))
    else : 
        return NbDaun(Left(T)) + NbDaun(Right(T))
    
def NbDaun1(T) :
    if IsOneElmt(T) :
        print(Akar(T))
        return 1
    if ((not IsEmpty(Left(T))) and (not IsEmpty(Right(T)))): 
        return NbDaun(Left(T)) + NbDaun(Right(T))
    elif (not IsEmpty(Left(T))) and (IsEmpty(Right(T))) :
        return NbDaun(Left(T))
    elif (IsEmpty(Left(T))) and (not IsEmpty(Right(T))) :
        return NbDaun(Right(T))



T = MakePB('A', MakePB('B', MakePB('C', [], []), MakePB('D', MakePB('E', [], []), MakePB('F', [], []))), MakePB('G', MakePB('H', [], []), []))
PrintBinaryTree(T)
print(T)
print("Jumlah daun di dalam Tree pake NB1: ", NbDaun1(T))
print("Jumlah node di dalam Tree: ", NbElmtTree(T))
print("Jumlah daun di dalam Tree: ", NbDaun(T))
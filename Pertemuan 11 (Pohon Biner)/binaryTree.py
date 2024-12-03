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
    if IsOneElmt(T) :
        print(Akar(T))
        return 1
    if ((not IsEmpty(Left(T))) and (not IsEmpty(Right(T)))): 
        return NbDaun(Left(T)) + NbDaun(Right(T))
    elif (not IsEmpty(Left(T))) and (IsEmpty(Right(T))) :
        return NbDaun(Left(T))
    elif (IsEmpty(Left(T))) and (not IsEmpty(Right(T))) :
        return NbDaun(Right(T))


def NbDaun1(P):
    if IsOneElmt(P):
        return 1
    elif IsBiner(P):
        return NbDaun1(Left(P)) + NbDaun1(Right(P))
    elif IsUnerLeft(P):
        return NbDaun1(Left(P))
    elif IsUnerRight(P):
        return NbDaun1(Right(P))


def IsMember(P, X):
    if IsOneElmt(P):
        return Akar(P) == X
    elif Akar(P) == X:
        return True
    elif IsBiner(P):
        return IsMember(Left(P), X) or IsMember(Right(P), X)
    elif IsUnerLeft(P):
        return IsMember(Left(P), X)
    elif IsUnerRight(P):
        return IsMember(Right(P), X)


def IsSkewLeft(P):
    if IsOneElmt(P):
        return True
    else:
        return IsUnerLeft(P)


def IsSkewRight(P):
    if IsOneElmt(P):
        return True
    else:
        return IsUnerRight(P)


def max2(a, b):
    return a if a > b else b


def Level(P, X, lvl):
    if IsTreeEmpty(P):
        return 0
    elif Akar(P) == X:
        return lvl
    else:
        return max2(Level(Left(P), X, lvl + 1), Level(Right(P), X, lvl + 1))


def LevelOfX(P, X):
    if IsTreeEmpty(P):
        return 0
    elif Akar(P) == X:
        return 0
    else:
        return Level(P, X, 0)


def AddDaunTerkiri(P, X):
    if IsTreeEmpty(P):
        return MakePB(X, [], [])
    elif IsUnerRight(P):
        return MakePB(Akar(P), Left(P), AddDaunTerkiri(Right(P), X))
    else:
        return MakePB(Akar(P), AddDaunTerkiri(Left(P), X), Right(P))


def AddDaun(P, X, Y, Kiri):
    if IsTreeEmpty(P):
        return P
    elif Akar(P) == X:
        if Kiri:
            return MakePB(X, MakePB(Y, [], []), Right(P))
        else:
            return MakePB(X, Left(P), MakePB(Y, [], []))
    else:
        return MakePB(
            Akar(P), AddDaun(Left(P), X, Y, Kiri), AddDaun(Right(P), X, Y, Kiri)
        )


def DelDaunTerkiri(P):
    if IsOneElmt(P):
        return []
    elif IsUnerRight(P):
        return MakePB(Akar(P), Left(P), DelDaunTerkiri(Right(P)))
    else:
        return MakePB(Akar(P), DelDaunTerkiri(Left(P)), Right(P))


def DelDaun(P, X):
    if IsTreeEmpty(P):
        return P
    elif Akar(P) == X:
        return []
    else:
        return MakePB(Akar(P), DelDaun(Left(P), X), DelDaun(Right(P), X))
    

def AddX(P, X):
    if IsEmpty(P):
        return MakePB(X, [], [])
    else:
        if X > Akar(P):
            return MakePB(Akar(P), Left(P), AddX(Right(P), X))
        else:
            return MakePB(Akar(P), AddX(Left(P), X), Right(P))


def Delete(P, X):
    if IsEmpty(P):
        return []
    else:
        if Akar(P) == X:
            if IsEmpty(Left(P)) and IsEmpty(Right(P)):
                return []
            #elif not IsEmpty(Left(P)) and not IsEmpty(Right(P)) :

            else:
                if IsEmpty(Left(P)):
                    return Right(P)
                    #return MakePB(Akar(Right(P)), Left(P), Right(Right(P)))
                else:
                    return Left(P)
                    #return MakePB(Akar(Left(P)), Left(Left(P)), Right(P))

        elif X >= Akar(P):
            return MakePB(Akar(P), Left(P), Delete(Right(P), X))
        else:
            return MakePB(Akar(P), Delete(Left(P), X), Right(P)) 


def BSearchX(BST, x):
    if Akar(BST) == x:
        return True
    elif IsOneElmt(BST):
        return False
    elif IsBiner(BST):
        return BSearchX(Left(BST),x) or BSearchX(Right(BST),x)
    elif IsUnerLeft(BST):
        return BSearchX(Left(BST),x)
    elif IsUnerRight(BST):
        return BSearchX(Right(BST),x)


def MakeListDaun(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    else:
        return MakeListDaun(Left(P)) + MakeListDaun(Right(P))


def MakeListPreOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        return [Akar(P)] + MakeListPreOrder(Left(P)) + MakeListPreOrder(Right(P))


def MakeListPostOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        return MakeListPostOrder(Left(P)) + MakeListPostOrder(Right(P)) + [Akar(P)]


def MakeListInOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        return MakeListInOrder(Left(P)) + [Akar(P)] + MakeListInOrder(Right(P))


def MakeListLevel(P, N):
    if IsTreeEmpty(P):
        return []
    elif N == 0:
        return [Akar(P)]
    else:
        return MakeListLevel(Left(P), N - 1) + MakeListLevel(Right(P), N - 1)


# APLIKASI

T = MakePB('A', MakePB('B', MakePB('C', [], []), MakePB('D', MakePB('E', [], []), MakePB('F', [], []))), MakePB('G', MakePB('H', [], []), []))
PrintBinaryTree(T)
print(T)
print("Jumlah daun di dalam Tree pake NB1: ", NbDaun1(T))
print("Jumlah node di dalam Tree: ", NbElmtTree(T))
print("Jumlah daun di dalam Tree: ", NbDaun(T))
print("Apakah 1 ada di dalam Tree: ", IsMember(T, 'A'))
print("Jumlah level dari 'A' di dalam Tree: ", LevelOfX(T, 'A'))
print("Apakah Tree skew ke kiri: ", IsSkewLeft(T))
print("Apakah Tree skew ke kanan: ", IsSkewRight(T))
print("Tambah daun terkiri: ", AddDaunTerkiri(T, 'I'))
print("Tambah daun: ", AddDaun(T, 'B', 'I', True))
print("Hapus daun terkiri: ", DelDaunTerkiri(T))
print("Hapus daun: ", DelDaun(T, 'B'))
print("Buat list daun: ", MakeListDaun(T))
print("Buat list pre order: ", MakeListPreOrder(T))
print("Buat list post order: ", MakeListPostOrder(T))
print("Buat list in order: ", MakeListInOrder(T))
print("Buat list level: ", MakeListLevel(T, 2))
print("Tambah X: ", AddX(T, 'Z'))
print("Delete X: ", Delete(T, 'B'))
print("Apakah F ada di dalam Tree: ", BSearchX(T, 'F'))
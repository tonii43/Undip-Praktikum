from binaryTree import *
from ListOfList1 import *

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
 
T = AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 200), 100),60),120)
print(T)
PrintBinaryTree(T)
PrintBinaryTree(Delete(T, 50))
PrintBinaryTree(Delete(T, 40))
print(Delete(T, 50))

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
    
print(BSearchX(T, 50))
print(BSearchX(T, 55))
print(BSearchX(T, 60))
print(BSearchX(T, 65))
print(BSearchX(AddX([], 70), 70))
print(BSearchX(T, 75))
print(BSearchX(T, 80))
print(BSearchX(T, 100))
print(BSearchX(T, "Kak Indah"))
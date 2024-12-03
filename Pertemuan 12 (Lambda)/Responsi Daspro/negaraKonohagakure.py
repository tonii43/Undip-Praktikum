# Fungsi dan operator yang lain bisa ditambahkan sendiri
def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def IsEmpty(L):
    return L == []

def isTreeNEmpty(PN):
    return PN == []

def akar(PN):
    return PN[0]

def anak(PN):
    return PN[1]

# def IsOneElmt(PN):
#     return (isTreeNEmpty(PN) == False) and (isTreeNEmpty(anak(PN)) == True)

def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L)==[] and Head(L)==[]

def max2(a, b):
    if a > b:
        return a
    else:
        return b

def maxRekursif(S):
    if IsEmpty(S):
        return 0
    elif IsOneElmt(S):
        return FirstElmt(S)
    else:
        return max2(FirstElmt(S), maxRekursif(Tail(S)))

def level(L):
    if IsEmpty(L):
        return 0
    else:
        return maxRekursif(FirstElmt(L)) + level(Tail(L))
    
def biaya(L):
    return level(L) * 1000000

# APLIKASI

import ast
list_of_list = ast.literal_eval(input())
print(biaya(list_of_list))
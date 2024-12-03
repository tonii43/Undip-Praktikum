# Fungsi untuk mengecek bilangan prima secara rekursif
def IsPrima(n, i=2):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % i == 0:
        return False
    elif i * i > n:
        return True
    else:
        return IsPrima(n, i + 1)
    
# Fungsi Antara
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

def isOneElmt(PN):
    return (isTreeNEmpty(PN) == False) and (isTreeNEmpty(anak(PN)) == True)

def IsAtom(S):
    return type(S) != list

def IsList(S):
    return type(S) == list

# Fungsi Jumlah Prima
def jumlahPrima(S):
    if IsEmpty(S):
        return 0
    elif IsAtom(FirstElmt(S)):
        if IsPrima(FirstElmt(S)):
            return FirstElmt(S) + jumlahPrima(Tail(S))
        else:
            return jumlahPrima(Tail(S))
    elif IsList(FirstElmt(S)):
        if IsPrima(FirstElmt(FirstElmt(S))):
            return FirstElmt(FirstElmt(S)) + jumlahPrima(Tail(FirstElmt(S))) + jumlahPrima(Tail(S))
        else:
            return jumlahPrima(Tail(FirstElmt(S))) + jumlahPrima(Tail(S))
        
# APLIKASI
import ast

list_of_list = ast.literal_eval(input())
print(jumlahPrima(list_of_list))
#NAMA: Muhammad Dimas Arya Putra
#NIM : 24060124130062

# DEFINISI DAN SPESIFIKASI# tail(L): List --> List
# tail(L) List dengan menghilangkan elemen pertamanya
def tail(L):
    return L[1:]

# DEFINISI DAN SPESIFIKASI
# firstElmt(L): List --> elemen
# firstElmt(L) Menampilkan elemen pertama dari List
def firstElmt(L):
    return L[0]

# DEFINISI DAN SPESIFIKASI
# isEmpty(L): List --> boolean
# isEmpty(L) mengecek apakah List kosong
def isEmpty(L):
    return L == []

def IsInteger(S):
    return type(S) == int

def IsListInteger(L):
    if isEmpty(L):
        return True
    elif IsInteger(firstElmt(L)):
        return IsListInteger(tail(L))
    else:
        return False
    
def SumList(L):
    if isEmpty(L):
        return 0
    elif IsListInteger(L):
        return firstElmt(L) + SumList(tail(L))
    else:
        return "males ah!"

# APLIKASI
print(SumList([int(x) if x.isdigit() else x for x in input().split()]))
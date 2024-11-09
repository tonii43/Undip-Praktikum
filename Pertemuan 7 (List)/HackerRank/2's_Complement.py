# Nama/NIM: Muhammad Dimas Arya Putra/24060124130062
# Tanggal: 29 Oktober 2024

# REALISASI {manfaatkan fungsi yang telah dipelajari, fungsi2 di bawah tidak harus digunakan semua}
def Konsi(y,x):
    return y + [x]

def Konso(y,x):
    return [y] + x

def FirstElmt(x):
    if x != []:    
        return x[0]

def Tail(x):
    if x != []:
        return x[1:]

def Head(x):
    if x != []:
        return x[:-1]

def IsEmpty(x):
    if x == []:
        return True
    else:
        return False
    
def LastElmt(x):
    if x != []:
        return x[-1]


def NbElmnt(x):
    if IsEmpty(x):
        return 0
    else:
        return 1 + NbElmnt(Tail(x))
  
# tulis jawaban di sini
def Balikin(B):
    if IsEmpty(B):
        return []
    else:
        if LastElmt(B) == 0:
            return Konsi(Balikin(Head(B)), 1)
        else:
            return Konsi(Balikin(Head(B)), 0)

def Nambah1(B):
    if IsEmpty(B):
        return [1]
    elif LastElmt(B) == 0:
        return Konsi(Head(B), 1)
    else:
        return Konsi(Nambah1(Head(B)), 0)
    
def AkhirnyaNambahBeneran(B):
    return Nambah1(Balikin(B))

def Penjumlahan(A, B):
    if IsEmpty(A) and IsEmpty(B):
        return []
    elif IsEmpty(A):
        return B
    elif IsEmpty(B):
        return A
    elif LastElmt(A) + LastElmt(B) == 2:
        return Konsi(Penjumlahan(Penjumlahan(Head(A), Head(B)), [1]), 0)
    else:
        return Konsi(Penjumlahan(Head(A), Head(B)), (LastElmt(A) + LastElmt(B)) % 2)

def bit5(L):
    if NbElmnt(L) <= 5:
        return L
    else:
        return bit5(Tail(L))
    
def twoscomp(A, B):
    return bit5(Penjumlahan(A, AkhirnyaNambahBeneran(B)))

# APLIKASI
print(twoscomp([1,0,1,1,0],[1,0,0,0,1]))

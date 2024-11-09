def Konso(e,L):
    return [e]+L

def Konsi(L,e):
    return L + [e]

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def Laprak(R, N):
    if IsEmpty(R) or IsEmpty(N):
        return 0
    elif FirstElmt(R) == 1 and FirstElmt(N) >= 90:
        return 1 + Laprak(Tail(R), Tail(N))
    else:
        return Laprak(Tail(R), Tail(N))
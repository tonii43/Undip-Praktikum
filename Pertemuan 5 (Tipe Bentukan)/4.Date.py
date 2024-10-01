def MakeTanggal(h, b, t):
    return [h, b, t]

def hari(d):
    return d[0]

def bulan(d):
    return d[1]

def tahun(d):
    return d[2]

def kabisat(t):
    return (t % 4 == 0 and t % 100 != 0) or (t % 400 == 0)

def returnMonth(dpm):
    if (1 <= dpm <= 32 or dpm == 0):
        return 1
    elif (32 < dpm <= 60):
        return 2
    elif (60 < dpm <= 91):
        return 3
    elif (91 < dpm <= 121):
        return 4
    elif (121 < dpm < 152):
        return 5
    elif (152 < dpm <= 182):
        return 6
    elif (182 < dpm <= 213):
        return 7
    elif (213 < dpm <= 244):
        return 8
    elif (244 < dpm <= 274):
        return 9
    elif(274 < dpm <= 305):
        return 10
    elif (305 < dpm <= 335):
        return 11
    elif (335 < dpm <= 367):
        return 12
    
def dpm(m):
    if (m == 1):
        return 1
    elif (m == 2):
        return 32
    elif (m == 3):
        return 60
    elif (m == 4):
        return 91
    elif (m == 5):
        return 121
    elif (m == 6):
        return 152
    elif (m == 7):
        return 182
    elif (m == 8):
        return 213
    elif (m == 9):
        return 244
    elif (m == 10):
        return 274
    elif (m == 11):
        return 305
    elif (m == 12):
        return 335
    
def HariKe1900(d):
    if kabisat(tahun(d)) and bulan(d) > 2:
        return dpm(bulan(d)) + hari(d)
    else:
        return dpm(bulan(d)) + hari(d) - 1
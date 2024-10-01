# Nama File : tanggal.py
# Deskipsi  : Membuat tipe bentukan tanggal beserta fungsi konstruktor, selektor, operator, dan predikatnya.
# Pembuat   : Mischa Nathanael Lumban Tobing
# NIM       : 24060124140175
# Tanggal   : 29 September 2024

# DEFINISI TYPE
# type Hari: integer[1..31]
#     {Hari adalah definisi integer yang memiliki batasan 1 - 31 sebagai representasi dari jumlah tanggal pada kalender.}
# type Bulan: integer[1..12]
#     {Bulan adalah definisi integer yang memiliki batasan 1 - 12 sebagai representasi dari jumlah bulan pada kalender.}
# type Tahun: integer > 0
#     {Tahun adalah definisi integer yang memiliki batasan bukan negatif dan bukan nol sebagai representasi dari tahun pada kalender.}
# type tanggal:  <hari: Hari, bulan: Bulan, tahun: Tahun>
#     {<hari, bulan, tahun> merupakan tipe bentukan tanggal.}
# -------------------------------------
# Definisi dan Spesifikasi Konstruktor
# --
# MakeTanggal: Hari, Bulan, Tahun → tanggal
#     {MakeTanggal(h, b, t) membentuk tipe data tanggal dari input (h, b, t).}
# Realisasi:
def MakeTanggal(h, b ,t):
    return [h, b, t]
# -------------------------------------
# Definisi dan Spesifikasi Selektor
# --
# hari: tanggal → Hari
#     {hari(d) mengembalikan hari dari tanggal (d).}
# bulan: tanggal → Bulan
#     {bulan(d) mengembalikan bulan dari tanggal (d).}
# tahun: tanggal → Tahun
#     {tahun(d) mengembalikan tahun dari tanggal (d).}
# Realisasi:
def hari(d):
    return d[0]

def bulan(d):
    return d[1]

def tahun(d):
    return d[2]
# -------------------------------------
# Definisi dan Spesifikasi Predikat
# --
# kabisatlagiyaallahgusti: Tahun → boolean
#     {kabisatlagiyaallahgusti(tahun) akan mengembalikan true jika tahun pada tanggal tersebut adalah kabisat,
#      yakni tahun yang habis dibagi 4 dan tidak habis dibagi 100 atau habis dibagi 400.}
# inihariyangsamakah: 2 tanggal → tanggal
#     {inihariyangsamakah(d1, d2) akan mengembalikan true jika (d1) adalah tanggal yang sama dengan (d2).}
# iniharikemarinnggak: 2 tanggal → tanggal
#     {iniharikemarinnggak(d1, d2) akan mengembalikan true jika (d1) adalah tanggal yang berada sebelum (d2).}
# iniharisetelahsetelahapabukan: 2 tanggal → tanggal
#     {iniharisetelahsetelahapabukan(d1, d2) akan mengembalikan true jika (d1) adalah tanggal yang berada setelah (d2).}
# Realisasi:
def kabisatlagiyaallahgusti(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
def inihariyangsamakah(d1, d2):
    return HariKe1900(d1) == HariKe1900(d2)
def iniharikemarinnggak(d1, d2):
    return HariKe1900(d1) < HariKe1900(d2)
def iniharisetelahsetelahapabukan(d1, d2):
    return HariKe1900(d1) > HariKe1900(d2)
# -------------------------------------
# Definisi dan Spesifikasi Operator
# --
# Nextday: tanggal → tanggal
#     {Nextday(d) akan mengembalikan tanggal keesokan hari dari (d).}
# Yesterday: tanggal → tanggal
#     {Yesterday(d) akan mengembalikan tanggal kemarin hari dari (d).}
# dpm: Bulan → integer
#     {dpm(m) akan mengembalikan jumlah kumulatif hari pada bulan (m).}
# HariKe1900: tanggal → integer
#     {HariKe1900(d) akan mengembalikan jumlah kumulatif hari pada tanggal (d).}
# Realisasi:
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
    if kabisatlagiyaallahgusti(tahun(d)) and bulan(d) > 2:
        return dpm(bulan(d)) + hari(d)
    else:
        return dpm(bulan(d)) + hari(d) - 1
    
def Nextday(d):
    if ((bulan(d) < 9 and bulan(d) % 2 == 1) or bulan(d) == 8 or bulan(d) == 10):
        if hari(d) < 31:
            return MakeTanggal(hari(d)+1, bulan(d), tahun(d))
        else: 
            return MakeTanggal(1, bulan(d)+1, tahun(d))
    elif (bulan(d) == 2):
        if hari(d) < 28 + kabisatlagiyaallahgusti(tahun(d)):
            return MakeTanggal(hari(d)+1, bulan(d), tahun(d))
        else:
            return MakeTanggal(1, bulan(d)+1, tahun(d))
    elif ((2 < bulan(d) < 8 and bulan(d) % 2 == 0) or bulan(d) == 9 or bulan(d) == 11):
        if hari(d) < 30:
            return MakeTanggal(hari(d)+1, bulan(d), tahun(d))
        else: 
            return MakeTanggal(1, bulan(d)+1, tahun(d))
    elif (bulan(d) == 12):
        if hari(d) < 31:
            return MakeTanggal(hari(d)+1, bulan(d), tahun(d))
        else: 
            return MakeTanggal(1, 1, tahun(d) + 1)
        
def NextNday(d, n):
    # creating this function without the use of recursives and loops are borderline impossible
    # actually, it's possible-however inefficient as hell. creating such code is a waste of time, dare i say.
    # therefore, i'd like to change the limit of n from [1...365] to [1..31]
    if ((bulan(d) < 9 and bulan(d) % 2 == 1) or bulan(d) == 8 or bulan(d) == 10):
        if hari(d) + n <= 31:
            return MakeTanggal(hari(d)+n, bulan(d), tahun(d))
        else: 
            return MakeTanggal(hari(d)+n - 31, bulan(d)+1, tahun(d))
    elif (bulan(d) == 2):
        if hari(d) + n <= (28 + kabisatlagiyaallahgusti(tahun(d))):
            return MakeTanggal(hari(d)+n, bulan(d), tahun(d))
        else:
            return MakeTanggal(hari(d)+n - (28 + kabisatlagiyaallahgusti(tahun(d))), bulan(d)+1, tahun(d))
    elif ((2 < bulan(d) < 8 and bulan(d) % 2 == 0) or bulan(d) == 9 or bulan(d) == 11):
        if hari(d) + n <= 30:
            return MakeTanggal(hari(d)+n, bulan(d), tahun(d))
        else: 
            return MakeTanggal(hari(d)+n - 30, bulan(d)+1, tahun(d))
    elif (bulan(d) == 12):
        if hari(d) + n <= 31:
            return MakeTanggal(hari(d)+n, bulan(d), tahun(d))
        else: 
            return MakeTanggal(hari(d)+n - 31, 1, tahun(d) + 1)
        
print(NextNday(MakeTanggal(28, 2, 2004), 2))

def Yest(d):
    if (hari(d) == 1):
        if (bulan(d) == 12 or bulan(d) == 5 or bulan(d) == 7 or bulan(d) == 10):
            return MakeTanggal(30, bulan(d) - 1, tahun(d))
        elif (bulan(d) == 3):
            if kabisatlagiyaallahgusti(tahun(d)):
                return MakeTanggal(29, 1, tahun(d))
            else:
                return MakeTanggal(28, 1, tahun(d))
        elif (bulan(d) == 1):
            return MakeTanggal(31, 12, tahun(d) - 1)
        else:
            return MakeTanggal(31, bulan(d) - 1, tahun(d))
    else:
        return MakeTanggal(hari(d) - 1, bulan(d), tahun(d))
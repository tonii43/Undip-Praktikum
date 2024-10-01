# Nama File : 5.DataMahasiswa.py
# Deskripsi : membuat tipe bentukan point beserta konstruksi dan selektornya serta pengaplikasiannya
# Pembuat   : Muhammad Dimas Arya Putra - 24060124130062
# Tanggal   : 29 September 2023

# DEFINISI TYPE TANGGAL LAHIR
# type TGL : <d:integer[1..31], m:integer[1..12], y:integer > 0 >
# {<d, m, y> adalah sebuah tanggal lahir, dengan d adalah tanggal, y adalah bulan, dan y adalah tahun}

# DEFINISI TYPE MHS1
# type MHS1 : <x:string, y:string, z:TGL>
# {<x, y, z> adalah sebuah data informasi dasar, dengan x adalah NIM, y adalah Nama, dan z adalah tanggal lahir mahasiswa}

# DEFINISI TYPE MHS2
# type MHS2 : <x:string, y:string, z:integer>
# {<x, y, z> adalah sebuah data informasi nilai, dengan x adalah NIM, y adalah KodeMatkul, dan z adalah Nilai}

# DEFINISI TYPE MHS3
# type MHS3 : <x:string, y:string>
# {<x, y> adalah sebuah data informasi matkul, dengan x adalah KodeMatkul dan y adalah NamaMatkul}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR

# MakeTGL: integer[1..31], integer[1..12], integer > 0 --> TGL
# { MaketanggalLahir(d, m, y) membentuk sebuah type bentukan tanggal lahir dengan d adalah tanggal, m adalah bulan, dan y adalah tahun} 
# Realisasi dalam Python
def makeTGL(d, m, y):
    return [d, m, y]

# MakeMHS1: 2 string, TGL --> MHS1
# { MakeMHS1(x, y, z) membentuk sebuah type bentukan informasi dasar dengan x adalah NIM, y adalah Nama, dan z adalah tanggal lahir mahasiswa} 
# Realisasi dalam Python
def makeMHS1(x, y, z):
    return [x, y, z]

# MakeMHS2: 2 string, integer --> MHS2
# { MakeMHS2(x, y, z) membentuk sebuah type bentukan informasi nilai dengan x adalah NIM, y adalah KodeMatkul, dan z adalah Nilai} 
# Realisasi dalam Python
def makeMHS2(x, y, z):
    return [x, y, z]

# MakeMHS3: 2 string --> MHS3
# { MakeMHS1(x, y) membentuk sebuah type bentukan informasi matkul dengan x adalah KodeMatkul dan y adalah NamaMatkul} 
# Realisasi dalam Python
def makeMHS3(x, y):
    return [x, y]

# DEFINISI DAN SPESIFIKASI SELEKTOR MHS1
# NIM: MHS1 --> string
# {NIM(P) memberikan NIM MHS1 dari P}
# Realisasi dalam Python
# def NIM(P):
#     return P[0]

# Nama: MHS1 --> string
# {Nama(P) memberikan Nama MHS1 dari P}
# Realisasi dalam Python
# def Nama(P):
#     return P[1]

# TGL: MHS1 --> string
# {TGL(P) memberikan tanggal lahir MHS1 dari P}
# Realisasi dalam Python
# def TGL(P):
#     return P[2]

# InfoMHS1: MHS1 --> string
# {InfoMHS1(P) memberikan informasi dasar mahasiswa P}
# Realisasi dalam Python
# def infoMHS1(P):
#     return f"{NIM(P), Nama(P), TGL(P)}" 

# DEFINISI DAN SPESIFIKASI SELEKTOR MHS2
# NIM: MHS2 --> string
# {NIM(P) memberikan NIM MHS2 dari P}
# Realisasi dalam Python
def NIM(P):
    return P[0]

# Nama: MHS2 --> string
# {Nama(P) memberikan KodeMatkul MHS2 dari P}
# Realisasi dalam Python
def KodeMatkul(P):
    return P[1]

# TGL: MHS2 --> integer
# {TGL(P) memberikan Nilai MHS2 dari P}
# Realisasi dalam Python
def Nilai(P):
    return P[2]

# InfoMHS2: MHS2 --> string
# {InfoMHS2(P) memberikan informasi nilai mahasiswa P}
# Realisasi dalam Python
def infoMHS2(P):
    return f"{NIM(P), KodeMatkul(P), Nilai(P)}" 

# DEFINISI DAN SPESIFIKASI SELEKTOR MHS3
# NIM: MHS3 --> string
# {NIM(P) memberikan KodeMatkul MHS3 dari P}
# Realisasi dalam Python
# def KodeMatkul(P):
#     return P[0]

# Nama: MHS3 --> string
# {Nama(P) memberikan NamaMatkul MHS3 dari P}
# Realisasi dalam Python
# def NamaMatkul(P):
#     return P[1]

# InfoMHS3: MHS3 --> string
# {InfoMHS3(P) memberikan informasi matkul mahasiswa P}
# Realisasi dalam Python
# def infoMHS3(P):
#     return f"{KodeMatkul(P), NamaMatkul(P)}" 

# DEFINISI DAN SPESIFIKASI OPERATOR
# hitungRangeNilai: 2 MHS2 --> string
# {hitungRangeNilai(M1, M2) menghasilkan kode matkul serta range antara nilai tertinggi dan nilai terendah dari nilai mahasiswa M1 dan M2.}
# Realisasi dalam Python

def NilaiMaks(M1,M2):
    return max(Nilai(M1), Nilai(M2))

def NilaiMin(M1,M2):
    return min(Nilai(M1), Nilai(M2))

def RangeNilai(M1,M2):
    return abs(Nilai(M1) - Nilai(M2))

def hitungRangeNilai(M1, M2):
    return [KodeMatkul(M1), NilaiMaks(M1, M2), NilaiMin(M1, M2), RangeNilai(M1, M2)]


#APLIKASI
print(hitungRangeNilai(makeMHS2(24060124130062, 567, 98), makeMHS2(24060124130062, 567, 90))) #--> [567, 98, 90, 8]
print(hitungRangeNilai(makeMHS2(24060124140149, 948, 100), makeMHS2(24060124130062, 567, 45))) #--> [948, 100, 45, 55]
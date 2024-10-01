#membuat sebuah fungsi yang mengembalikan hasil dan menampilkannya pada output
def fx2(x):
    return x*x

hasil = fx2(4)
print(hasil)

def fx3(x):
    return x*x*x
hasil1 = fx3(4)
print(hasil1)

def fx3V2(x):
    return fx2(x)*x
hasil2 = fx3V2(10)
print(hasil2)

#membuat fungsi dengan 2 parameter
def isOrigin(absis,ordinat):
    return absis ==0 and ordinat==0
print(isOrigin(0,0))
print(isOrigin(1,0))

#membuat pangkat dengan library(gblh kalo awal praktikum)
x = 5**2
print(x)

#membuat akar dengan library
y = 9**0.5 #diakalin pake koma
print(y)

#mencari nilai max dari suatu parameter
def max2(x,y):
    return (int)((x + y) + (fx2(x-y))**0.5) // 2
print(max2(1000, 32313))
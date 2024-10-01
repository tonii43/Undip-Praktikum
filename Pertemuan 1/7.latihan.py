#nomer 2 (Contoh-5) = Apakah positif?
nilai = 2
def positif(x):
    return x > 0

print(positif(nilai))

#nomer 3 (Contoh-7) = Apakah A?
huruf = 'A'
huruf1 = 'M'
huruf2 = 'a'
huruf3 = 'n'
def apakah(x):
    return x == 'a' or x == 'A'

#print(apakah(huruf))
#print(apakah(huruf1))
#print(apakah(huruf2))
#print(apakah(huruf3))

#nomer 4
def IsValid(x):
    return x > 4 and x < 10

print(IsValid(8))
print(IsValid(11))

#nomer 5
def LeastSquare(basePointX, basePointY, targetPointX, targetPointY):
    lengthX = targetPointX - basePointX
    lengthY = targetPointY - basePointY

    total = (lengthX**2) + (lengthY**2)

    return total ** 0.5

print(LeastSquare(1, 1, 4, 5))
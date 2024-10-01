# Ekspresi Kondisional

# Ekspresi kondisional memiliki domain fungsi untuk mendapatkan solusi,
# yang dipartisi untuk memenuhi kondisi tertentu.

# Notasi Fungsional        Phyton
# - depend on              - if-elif
# - if-then-else           - if-else

# Contoh:
# Python
def max2(a,b):
    if a >= b:
        return a
    else:
        return b
print(max2(10,11)) #output = 11

# Cara lain
def max2v2(a,b):
    return (a if a >= b else b)
print(max2v2(10,11)) #output = 11

# Contoh Depend-on di Python:
def max3(a,b,c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    elif (c>a) and (c>b):
        return c
print(max3(3,4,5)) #output = 5

# Nested If
# If-else bersarang (didalem if else lagi)

# Contoh:
def max3(a,b,c):
    if a>b :
        if a>c :
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
        
print(max3(3,4,5))
print(max3(2,6,19))
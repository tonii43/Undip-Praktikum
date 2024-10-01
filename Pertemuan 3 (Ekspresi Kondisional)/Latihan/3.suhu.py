def reamur(C):
    return 4/5 * C
def fahrenheit(C):
    return (9/5 * C) + 32
def kelvin(C):
    return C + 273.15

def suhu(C):
    return reamur(C), fahrenheit(C), kelvin(C)

print(suhu(9))
print(suhu(100.2))
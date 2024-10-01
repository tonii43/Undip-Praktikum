def fx2(x):
    return x*x
def jalanSemut1(x,y,z):
    return round(((fx2(x+y) + fx2(z))**0.5), 3)
def jalanSemut2(x,y,z):
    return round(((fx2(x+z) + fx2(y))**0.5), 3)
def jalanSemut3(x,y,z):
    return round(((fx2(y+z) + fx2(x))**0.5), 3)

def jalanSemut(x,y,z):
    return min(jalanSemut1(x,y,z), jalanSemut2(x,y,z), jalanSemut3(x,y,z))

print(jalanSemut(3,4,5))
print(jalanSemut(1,2,7))
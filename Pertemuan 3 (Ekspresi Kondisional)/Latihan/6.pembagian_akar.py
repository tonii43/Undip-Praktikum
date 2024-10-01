def fx2(x):
    return x*x
def x1(a,b,c):
    return (-b + (fx2(b) - 4*a*c)**0.5) / (2*a)
def x2(a,b,c):
    return (-b - (fx2(b) - 4*a*c)**0.5) / (2*a)
def pembagianakar(a,b,c):
    x1(a,b,c)
    x2(a,b,c)
    if (x1(a,b,c) > x2(a,b,c)):
        return x1(a,b,c)/x2(a,b,c)
    else:
        return x2(a,b,c)/x2(a,b,c)

print(pembagianakar(1,3,1))
print(pembagianakar(1,3,2))
print(pembagianakar(1,5,6))
print(pembagianakar(1,9,2))
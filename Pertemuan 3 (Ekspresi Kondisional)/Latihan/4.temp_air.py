def temp(C):
    if C < 0:
        return "es (padat)"
    elif 0 <= C and C <= 100:
        return "cair"
    else:
        return "uap"

print(temp(-10))
print(temp(0))
print(temp(10))
print(temp(100))
print(temp(150))
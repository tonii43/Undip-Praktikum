def fx2(x):
    return x*x
def f(x):
    return (3*fx2(x)) + (2*x) - 5
def gradien(x,y):
    return (f(x) - f(y)) / (x - y)

print(gradien(3,1))
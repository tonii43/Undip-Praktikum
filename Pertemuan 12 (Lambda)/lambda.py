x = lambda i : i + 1   

def sig1(a,b):
    if (a > b):
        return 0
    else:   
        return a + sig1(a+1, b)

print(sig1(2,5))

def id(i):
    return i

def p1(i):
    return i + 1

def sigma(a,b,f,s):
    if(a > b):
        return 0
    else:
        return f(a) +  sigma(s(a), b, f, s)
    
print(sigma(2, 5, id, p1))
print(sigma(2, 5, lambda i: i, lambda i: i +1))

x = lambda i: i+1
b = lambda a, a1: a if a < a1 else "salah"
print(x(5))
print(b(5,6))
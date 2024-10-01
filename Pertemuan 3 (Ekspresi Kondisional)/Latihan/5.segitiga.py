def segitiga(a,b,c):
    if a == b and b == c:
        return "Segitiga Sama Sisi"
    elif a == b or b == c or a == c:
        return "Segitiga Sama Kaki"
    else:
        return "Segitiga Sembarang"
    
print(segitiga(1,2,3))
print(segitiga(1,1,3))
print(segitiga(3,3,3))
print(segitiga(1,2,2))
print(segitiga(1,2,1))
#operator and (jika ingin true, berarti ekspresi harus benar semua)
benar = 13 > 7 and 3 > 1
salah = 13 < 7 and 3 > 1
print(benar)
print(salah)

#operator or (jika ingin true, hanya perlu salah satu dari ekspresi benar)
benar = 13 > 7 or 3 < 1
benar2 = 13 > 7 or 3 > 1
salah = 13 < 7 or 3 < 1
print(benar, benar2, salah)
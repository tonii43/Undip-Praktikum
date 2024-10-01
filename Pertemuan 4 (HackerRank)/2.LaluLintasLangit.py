def monitor_pesawat(x,y,z):
    if y > 900 or y < 200:
        return "Kecepatan Berbahaya"
    elif x > 12000:
        return "Terlalu Tinggi"
    elif z < 20:
        return "Bahan Bakar Rendah"
    elif x < 5000 and y >= 200 and y <= 900 and z > 50:
        return "Aman untuk Mendarat"
    else:
        return "Berjalan Normal"
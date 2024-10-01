def PekanSebelum(D):
    if D == "senin":
        return (5000 + 6000 + 4000)/3
    elif D == "selasa":
        return (7000 + 5000 + 2000)/3
    elif D == "rabu":
        return (4500 + 3500 + 3000)/3
    elif D == "kamis":
        return (2900 + 2100 + 2000)/3
    elif D == "jumat":
        return (3000 + 3000 + 3000)/3
    elif D == "sabtu":
        return (2000 + 2500 + 2300)/3
    elif D == "minggu":
        return (1100 + 900 + 1000)/3
def Waktu(X,Y):
    return abs(X-Y)
def PerkiraanAhli(AS, AM, AIP):
    return max(AS, AM, AIP) - min(AS, AM, AIP)
def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
    # Full siang
    if (X >= SR and X < SS and Y > SR and Y <= SS):
        return round((Waktu(X,Y) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D), 5)
    # Sebelum matahari terbit dan sebelum matahari terbenam
    elif (X < SR and Y <= SS and Y > SR):
        return round(((((Waktu(X,SR) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D)) * R/100) + ((Waktu(SR,Y) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D)))/2, 5)
    # Setelah matahari terbit dan setelah matahari terbenam
    elif (X >= SR and X < SS and Y > SS and Y >= SR):
        return round((((Waktu(X,SS) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D)) + (((Waktu(SS,Y) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D)) * R/100))/2, 5)
    # Subuh sampai malam lagi
    elif (X < SR and Y > SS and Y >= SR):
        return round(((((Waktu(X,SR) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D)) * R/100) + (((Waktu(SS,SR) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D))) + (((Waktu(SS,Y) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D)) * R/100))/3, 5)
    # Full malam atau Full Subuh
    elif (X >= SS and Y >= SS) or (X <= SR and Y <= SR):
        return round(((Waktu(X,Y) * PerkiraanAhli(AS,AM,AIP))/PekanSebelum(D)) * R/100, 5)
    
print(EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75))
def jam(j,m,s):
    if j <= 24 and j >= 0:
        if m <= 59 and m >= 0:
            if s <= 59 and s >= 0:
                return(f"Jam: {j}, Menit: {m}, Detik: {s}")
            else:
                return("Waktu tidak valid")
        else:
            return("Waktu tidak valid")
    else:
        return("Waktu tidak valid")
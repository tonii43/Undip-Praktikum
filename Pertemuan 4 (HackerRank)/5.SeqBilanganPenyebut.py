def denumeratorSeq(x):
    if ((10**(len(x))-1)/int(x))%1 == 0:
        return f"Ada: {((10**(len(x))-1)//int(x))}"
    else:
        return "Tidak ada"

print(denumeratorSeq('3'))
print(denumeratorSeq('166'))
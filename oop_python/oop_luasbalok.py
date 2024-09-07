class Luasbalok:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar


balok = Luasbalok(20, 10)
print("Panjang balok:", balok.panjang)
print("Lebar balok:", balok.lebar)
print("Luas balok : ", balok.panjang * balok.lebar)

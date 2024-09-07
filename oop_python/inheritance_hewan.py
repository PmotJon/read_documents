class Hewan:
    # konstruktor
    def __init__(self, nama):
        self.nama = nama

        # metode

    def jalankan(self):
        print("Hewan ini sedang berjalan")


# inheritance
class Anjing(Hewan):
    def jalankan(self):
        print("Anjing ini sedang berlari dngn kecepatan tinggi")


class Kucing(Hewan):
    def jalankan(self):
        print("Kucing ini sedang mengejar dngn  kecepatan tinggi ")


Animal = Hewan("Hewan")
Animal.jalankan()

Dog = Anjing("Hewan pribadi")
Dog.jalankan()

cat = Kucing("Hewan liar")
cat.jalankan

class Mobil:
    # oop wajib constructor
    def __init__(self, warna, merk, nomor_polisi):
        # atributes
        self.warna = warna
        self.merk = merk
        self.nomor_polisi = nomor_polisi

    # metode(perilaku)
    def start(self):
        self.nyala = "Mobil bisa dinyalakan"

    def move(self):
        self.jalan = "Mobil jalan"

    def accelerate(self):
        self.jalan = "Mobil melaju 80 km/jam dalam waktu 50 detik"

    def stop(self):
        print("Mobil sedang dimatikan")


mobil_toyota = Mobil("Biru", "Toyota Avanza", "DD46738U")

print("Mencetak atribute mobil toyota: ")
print("warna:", mobil_toyota.warna)
print("merk:", mobil_toyota.merk)
print("Plat Mobil:", mobil_toyota.nomor_polisi)

print("-" * 40)
print("Mencetak perilaku mobil toyota: ")
mobil_toyota.start()
mobil_toyota.move()
mobil_toyota.accelerate()
mobil_toyota.stop()

mobil_honda = Mobil("Putih", "Honda Brio", "DD7627U")
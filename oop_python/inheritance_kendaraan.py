class Kendaraan:
    # konstruktor
    def __init__(self, nama):
        self.nama = nama

        # metode

    def jalankan(self):
        print("Kendaraan ini sedang berjalan")


# inheritance
class Mobil(Kendaraan):
    def jalankan(self):
        print("mobil ini sedang melaju dngn kecepatan tinggi")


class Motor(Kendaraan):
    def jalankan(self):
        print("Motor ini sedang digas dngn gigi kecepatan tinggi ")


vehicle = Kendaraan("Transportasi")
vehicle.jalankan()

car = Mobil("Transportasi pribadi")
car.jalankan()

motor = Motor("Roda dua")
motor.jalankan

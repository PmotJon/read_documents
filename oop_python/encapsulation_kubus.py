class Kubus:
    # setter
    def setRusuk(self, rusuk):
        self.rusuk = rusuk

    # methode private
    def volume(self):
        return self.rusuk**3

    # method publik
    def tampilInfo(self):
        print("Rusuk: ", self.rusuk)
        print("Rusuk: ", self.volume())


cube = Kubus()

cube.setRusuk(4)
cube.tampilInfo()

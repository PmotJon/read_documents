class Orang:
    # atributes setter
    def __init__(self) -> None:
        print("Daftar nama-nama yg belajar")

    # Contoh method setter
    def setName(self, nama):
        self.name = nama

    # Contoh method getter
    def getName(self):
        return self.name


saya = Orang()

saya.setName("Jon")
print(saya.getName())
saya.setName("Halip")
print(saya.getName())
saya.setName("lala")
print(saya.getName())

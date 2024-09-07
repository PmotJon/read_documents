class Indonesia:
    def ibukota(self):
        print("IKN adalah ibukota Indonesia.")

    def bahasa(self):
        print("Bahasa Indonesia adalah bahasa nasional Indonesia")


class Malaysia:
    def ibukota(self):
        print("Kuala Lumpur adalah ibukota Malaysia")

    def bahasa(self):
        print("Bahasa Melayu adalah bahasa nasional di Malaysia")


def informasi(negara):
    negara.ibukota()
    negara.bahasa()


Indo = Indonesia()
Malay = Malaysia()

informasi(Malay)
informasi(Indo)

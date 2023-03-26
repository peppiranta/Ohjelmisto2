import random


class Hissi:
    def __init__(self, ala, yla):
        self.ala = ala
        self.yla = yla
        self.kerros = ala

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.ala:
            kohdekerros = self.ala
        elif kohdekerros > self.yla:
            kohdekerros = self.yla

        while self.kerros < kohdekerros:
            self.kerros_ylos()
        while self.kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.yla:
            self.kerros += 1
        print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.ala:
            self.kerros -= 1
        print("Hissi on kerroksessa", self.kerros)


class Talo:
    def __init__(self, ala, yla, hisseja):
        self.hissit = []
        for i in range(hisseja):
            hissi = Hissi(ala, yla)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(0)


talo = Talo(1, 10, 3)

# Testataan talon hisseillä ajelemista
talo.aja_hissia(1, 7)
talo.aja_hissia(2, 3)
talo.aja_hissia(3, 10)

# Palohälytys!
print("Palohälytys! Kaikki hissit ajetaan pohjakerrokseen!")
talo.palohalytys()

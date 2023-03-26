class Hissi:
    def __init__(self, ala_kerros, yla_kerros):
        self.kerros = ala_kerros
        self.ala_kerros = ala_kerros
        self.yla_kerros = yla_kerros

    def kerros_ylos(self):
        if self.kerros < self.yla_kerros:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.kerros > self.ala_kerros:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros < kohde_kerros:
            self.kerros_ylos()
        while self.kerros > kohde_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, ala_kerros, yla_kerros, hissien_lukumaara):
        self.hissit = []
        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(ala_kerros, yla_kerros))
        self.ala_kerros = ala_kerros
        self.yla_kerros = yla_kerros

    def aja_hissia(self, hissin_numero, kohde_kerros):
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kohde_kerros)

# Testikoodi
talo = Talo(1, 10, 2)
talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)
talo.aja_hissia(0, 1)
